-- =============================================================
-- Produção (qgywucdnaeheqndcxtho): aplicar 0012, 0013 e 0014 + mover pg_net
-- Rodar no Supabase → SQL Editor, com o seletor de branch em **main**.
-- Tudo numa transação: se qualquer parte falhar, nada é aplicado.
-- Origem: repositório portal-municipal (mesmo SQL já aplicado na homologação).
-- =============================================================
begin;

-- ######## 0012_verificacao_links ########
-- =============================================================
-- 0012 · Verificação de links quebrados (RF18, D-31)
-- Toda semana (e quando alguém pede no painel) cada município ganha uma
-- verificação "pendente". A Edge Function verificar-links pega a verificação,
-- confere os links do conteúdo publicado em lotes e grava os problemas em
-- verificacao_problemas, que o painel mostra com o link para corrigir.
--
-- Como a Edge Function é chamada: o pg_cron, a cada minuto, só dispara a função
-- (pg_net) se há trabalho na fila. A função não recebe parâmetros nem segredo:
-- ela só processa o que está na fila, então chamá-la de fora não faz nada além
-- de adiantar o trabalho já pedido.
-- Configuração por projeto (interno.configuracao, não é segredo):
--   supabase_url  endereço do projeto (para chamar a Edge Function)
--   ambiente      'producao' ou 'homologacao' (qual domínio do portal usar nos links internos)
-- =============================================================

create table interno.configuracao (
  chave text primary key,
  valor text not null
);
alter table interno.configuracao enable row level security;

-- -------------------------------------------------------------
-- Verificação: situação, quem pediu, batimento (para retomar se a função cair)
-- -------------------------------------------------------------
alter table public.verificacoes_links
  add column status         text not null default 'pendente'
    check (status in ('pendente', 'processando', 'concluida', 'erro')),
  add column solicitado_por uuid default auth.uid() references auth.users on delete set null,
  add column atualizado_em  timestamptz not null default now(),
  add column erro           text;
-- Uma verificação em andamento por município.
create unique index verificacoes_links_uma_em_andamento on public.verificacoes_links (municipio_id)
  where status in ('pendente', 'processando');

alter table public.verificacao_problemas add column origem_titulo text;

-- Publicador pede uma verificação do próprio município (botão "Verificar agora").
create policy "verificacoes: publicador solicita" on public.verificacoes_links for insert to authenticated
  with check (public.pode_publicar(municipio_id) and status = 'pendente');
grant insert (municipio_id) on public.verificacoes_links to authenticated;

-- -------------------------------------------------------------
-- Fila de links de uma verificação. Só a chave de serviço (Edge Function) mexe.
-- -------------------------------------------------------------
create table public.verificacao_fila (
  id              bigint generated always as identity primary key,
  verificacao_id  uuid not null references public.verificacoes_links on delete cascade,
  url             text not null,      -- endereço a conferir (relativo já resolvido para o domínio do portal)
  url_original    text not null,      -- como está no conteúdo
  origem_tabela   text not null,
  origem_id       uuid not null,
  origem_titulo   text,
  verificado      boolean not null default false,
  reservado_ate   timestamptz,        -- lote em conferência por uma execução da função
  status_http     smallint,
  erro            text
);
create index on public.verificacao_fila (verificacao_id, verificado, url);
alter table public.verificacao_fila enable row level security;
revoke all on public.verificacao_fila from anon, authenticated;
grant select, insert, update, delete on public.verificacao_fila to service_role;

-- -------------------------------------------------------------
-- Início: reserva a verificação mais antiga e monta a fila a partir do conteúdo publicado.
-- Links para arquivos do próprio Storage são conferidos aqui mesmo (storage.objects),
-- sem requisição: são milhares e não precisam sair do banco.
-- -------------------------------------------------------------
create or replace function public.verificacao_iniciar()
returns table (verificacao_id uuid, municipio_id uuid, ja_iniciada boolean)
language plpgsql
security definer
set search_path = ''
as $$
#variable_conflict use_column
declare
  v_id      uuid;
  v_mid     uuid;
  v_status  text;
  v_base    text;
  v_storage text;
  v_amb     text := coalesce((select valor from interno.configuracao where chave = 'ambiente'), 'producao');
begin
  -- Retoma a que está em andamento (função caiu ou estourou o tempo); senão, a pendente mais antiga.
  select v.id, v.municipio_id, v.status into v_id, v_mid, v_status
    from public.verificacoes_links v
   where v.status = 'processando' or v.status = 'pendente'
   order by (v.status = 'processando') desc, v.iniciado_em
   limit 1
   for update skip locked;
  if v_id is null then return; end if;

  if v_status = 'processando' then
    update public.verificacoes_links set atualizado_em = now() where id = v_id;
    return query select v_id, v_mid, true;
    return;
  end if;

  select 'https://' || d.dominio into v_base from public.municipio_dominios d
   where d.municipio_id = v_mid and d.principal and d.ambiente::text = v_amb limit 1;
  v_storage := (select valor from interno.configuracao where chave = 'supabase_url') || '/storage/v1/object/public/midias/';

  insert into public.verificacao_fila (verificacao_id, url, url_original, origem_tabela, origem_id, origem_titulo)
  select v_id,
         -- Sem domínio no ambiente, o relativo fica como está e aparece como "endereço inválido".
         case when l.url like '/%' and l.url not like '//%' then coalesce(v_base || l.url, l.url)
              when l.url like '//%' then 'https:' || l.url
              else l.url end,
         l.url, l.tabela, l.id, l.titulo
    from (
      select 'publicacoes' tabela, p.id, p.titulo, (regexp_matches(p.corpo_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1] url
        from public.publicacoes p where p.municipio_id = v_mid and p.status = 'publicado'
      union all
      select 'documentos', d.id, d.titulo, (regexp_matches(d.descricao_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.documentos d where d.municipio_id = v_mid and d.status = 'publicado'
      union all
      select 'documentos', d.id, d.titulo, a.url_externa
        from public.documento_arquivos a join public.documentos d on d.id = a.documento_id
       where d.municipio_id = v_mid and d.status = 'publicado' and a.url_externa is not null
      union all
      select 'paginas', p.id, p.titulo, (regexp_matches(p.corpo_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.paginas p where p.municipio_id = v_mid and p.status = 'publicado'
      union all
      select 'servicos', s.id, s.titulo, (regexp_matches(coalesce(s.etapas_html, '') || coalesce(s.requisitos_html, ''), '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.servicos s where s.municipio_id = v_mid and s.status = 'publicado'
      union all
      select 'servicos', s.id, s.titulo, s.url_externa
        from public.servicos s where s.municipio_id = v_mid and s.status = 'publicado' and s.url_externa is not null
      union all
      select 'eventos', e.id, e.titulo, (regexp_matches(e.descricao_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.eventos e where e.municipio_id = v_mid and e.status = 'publicado'
      union all
      select 'eventos', e.id, e.titulo, e.url_externa
        from public.eventos e where e.municipio_id = v_mid and e.status = 'publicado' and e.url_externa is not null
      union all
      select 'perguntas_frequentes', f.id, f.pergunta, (regexp_matches(f.resposta_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.perguntas_frequentes f where f.municipio_id = v_mid and f.status = 'publicado'
      union all
      select 'orgaos', o.id, o.nome, (regexp_matches(coalesce(o.competencias_html, '') || coalesce(o.responsavel_curriculo_html, ''), '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.orgaos o where o.municipio_id = v_mid and o.ativo
      union all
      select 'destaques', x.id, x.titulo, x.url
        from public.destaques x where x.municipio_id = v_mid and x.status = 'publicado' and x.url is not null
             and (x.fim_em is null or x.fim_em > now())
      union all
      select 'menu_itens', m.id, m.rotulo, m.url from public.menu_itens m where m.municipio_id = v_mid and m.url is not null
      union all
      select 'transparencia_itens', t.id, t.titulo, t.url from public.transparencia_itens t where t.municipio_id = v_mid and t.ativo and t.url is not null
      union all
      select 'sistemas_externos', s.id, s.nome, s.url from public.sistemas_externos s where s.municipio_id = v_mid and s.ativo and s.url is not null
    ) l
   where l.url ~* '^(https?:|/)' ;

  -- Arquivos do próprio Storage: confere direto no banco.
  update public.verificacao_fila f
     set verificado = true,
         status_http = case when exists (
           select 1 from storage.objects o where o.bucket_id = 'midias' and o.name = substr(f.url, length(v_storage) + 1)
         ) then 200 else 404 end
   where f.verificacao_id = v_id and f.url like v_storage || '%';

  update public.verificacoes_links
     set status = 'processando', atualizado_em = now(),
         total_links = (select count(distinct url) from public.verificacao_fila where verificacao_id = v_id)
   where id = v_id;
  return query select v_id, v_mid, false;
end $$;

-- Próximo lote de endereços distintos ainda não conferidos; reserva por 3 min
-- (outra execução simultânea pega outros).
create or replace function public.verificacao_proximos(p_verificacao uuid, p_limite int default 100)
returns table (url text)
language plpgsql
security definer
set search_path = ''
as $$
#variable_conflict use_column
begin
  return query
  with lote as (
    select distinct f.url from public.verificacao_fila f
     where f.verificacao_id = p_verificacao and not f.verificado
       and (f.reservado_ate is null or f.reservado_ate < now())
     limit p_limite
  ), reservados as (
    update public.verificacao_fila f set reservado_ate = now() + interval '3 minutes'
      from lote where f.verificacao_id = p_verificacao and f.url = lote.url and not f.verificado
    returning f.url
  )
  select distinct r.url from reservados r;
  update public.verificacoes_links set atualizado_em = now() where id = p_verificacao;
end $$;

-- Resultado de um lote: [{url, status_http, erro}]
create or replace function public.verificacao_registrar(p_verificacao uuid, p_resultados jsonb)
returns void
language sql
security definer
set search_path = ''
as $$
  update public.verificacao_fila f
     set verificado = true, status_http = (r->>'status_http')::smallint, erro = r->>'erro', reservado_ate = null
    from jsonb_array_elements(p_resultados) r
   where f.verificacao_id = p_verificacao and f.url = r->>'url';
$$;

-- Fecha a verificação: só vira problema o que é falha de fato (404/410, erro do servidor,
-- endereço que não responde). 401/403/405/429 são bloqueios a robôs, não links quebrados.
create or replace function public.verificacao_concluir(p_verificacao uuid)
returns int
language plpgsql
security definer
set search_path = ''
as $$
declare v_problemas int;
begin
  if exists (select 1 from public.verificacao_fila where verificacao_id = p_verificacao and not verificado) then
    return -1;  -- ainda há links a conferir
  end if;
  insert into public.verificacao_problemas (verificacao_id, tipo, url, status_http, erro, origem_tabela, origem_id, origem_titulo)
  select p_verificacao,
         case when f.status_http in (404, 410) then 'link_quebrado' else 'pagina_indisponivel' end,
         f.url_original, f.status_http, f.erro, f.origem_tabela, f.origem_id, f.origem_titulo
    from public.verificacao_fila f
   where f.verificacao_id = p_verificacao
     and (f.status_http in (404, 410) or f.status_http >= 500 or (f.status_http is null and f.erro is not null));
  get diagnostics v_problemas = row_count;
  update public.verificacoes_links
     set status = 'concluida', concluido_em = now(), atualizado_em = now(), problemas = v_problemas
   where id = p_verificacao;
  delete from public.verificacao_fila where verificacao_id = p_verificacao;
  return v_problemas;
end $$;

revoke all on function public.verificacao_iniciar(), public.verificacao_proximos(uuid, int),
  public.verificacao_registrar(uuid, jsonb), public.verificacao_concluir(uuid) from public, anon, authenticated;
grant execute on function public.verificacao_iniciar(), public.verificacao_proximos(uuid, int),
  public.verificacao_registrar(uuid, jsonb), public.verificacao_concluir(uuid) to service_role;

-- -------------------------------------------------------------
-- Agendamento
-- -------------------------------------------------------------
-- Uma verificação pendente por município ativo (a do painel, se já houver, conta).
create or replace function interno.agendar_verificacoes()
returns void
language sql
security definer
set search_path = ''
as $$
  insert into public.verificacoes_links (municipio_id, status)
  select m.id, 'pendente' from public.municipios m where m.ativo
  on conflict do nothing;
$$;

-- Dispara as Edge Functions que têm trabalho na fila. Sem supabase_url configurado, não faz nada.
create or replace function interno.disparar_rotinas()
returns void
language plpgsql
security definer
set search_path = ''
as $$
declare v_url text := (select valor from interno.configuracao where chave = 'supabase_url');
begin
  if v_url is null then return; end if;
  -- Em andamento, a função retoma de onde parou. Sem batimento por 30 min (falha repetida): desiste;
  -- a verificação semanal seguinte tenta de novo.
  update public.verificacoes_links set status = 'erro', erro = 'interrompida sem batimento por 30 min'
   where status = 'processando' and atualizado_em < now() - interval '30 minutes';
  if exists (select 1 from public.verificacoes_links where status in ('pendente', 'processando')) then
    perform net.http_post(url := v_url || '/functions/v1/verificar-links', body := '{}'::jsonb,
                          headers := '{"Content-Type": "application/json"}'::jsonb, timeout_milliseconds := 1000);
  end if;
end $$;

revoke all on all functions in schema interno from public, anon, authenticated;

do $$
begin
  if exists (select 1 from pg_extension where extname = 'pg_cron') then
    -- Domingo, 3h de Brasília (6h UTC).
    perform cron.schedule('agendar-verificacoes', '0 6 * * 0', 'select interno.agendar_verificacoes()');
    perform cron.schedule('disparar-rotinas', '* * * * *', 'select interno.disparar_rotinas()');
  end if;
end $$;

insert into supabase_migrations.schema_migrations (version, name, statements)
values ('20261012000012', '0012_verificacao_links', array[$mig$-- =============================================================
-- 0012 · Verificação de links quebrados (RF18, D-31)
-- Toda semana (e quando alguém pede no painel) cada município ganha uma
-- verificação "pendente". A Edge Function verificar-links pega a verificação,
-- confere os links do conteúdo publicado em lotes e grava os problemas em
-- verificacao_problemas, que o painel mostra com o link para corrigir.
--
-- Como a Edge Function é chamada: o pg_cron, a cada minuto, só dispara a função
-- (pg_net) se há trabalho na fila. A função não recebe parâmetros nem segredo:
-- ela só processa o que está na fila, então chamá-la de fora não faz nada além
-- de adiantar o trabalho já pedido.
-- Configuração por projeto (interno.configuracao, não é segredo):
--   supabase_url  endereço do projeto (para chamar a Edge Function)
--   ambiente      'producao' ou 'homologacao' (qual domínio do portal usar nos links internos)
-- =============================================================

create table interno.configuracao (
  chave text primary key,
  valor text not null
);
alter table interno.configuracao enable row level security;

-- -------------------------------------------------------------
-- Verificação: situação, quem pediu, batimento (para retomar se a função cair)
-- -------------------------------------------------------------
alter table public.verificacoes_links
  add column status         text not null default 'pendente'
    check (status in ('pendente', 'processando', 'concluida', 'erro')),
  add column solicitado_por uuid default auth.uid() references auth.users on delete set null,
  add column atualizado_em  timestamptz not null default now(),
  add column erro           text;
-- Uma verificação em andamento por município.
create unique index verificacoes_links_uma_em_andamento on public.verificacoes_links (municipio_id)
  where status in ('pendente', 'processando');

alter table public.verificacao_problemas add column origem_titulo text;

-- Publicador pede uma verificação do próprio município (botão "Verificar agora").
create policy "verificacoes: publicador solicita" on public.verificacoes_links for insert to authenticated
  with check (public.pode_publicar(municipio_id) and status = 'pendente');
grant insert (municipio_id) on public.verificacoes_links to authenticated;

-- -------------------------------------------------------------
-- Fila de links de uma verificação. Só a chave de serviço (Edge Function) mexe.
-- -------------------------------------------------------------
create table public.verificacao_fila (
  id              bigint generated always as identity primary key,
  verificacao_id  uuid not null references public.verificacoes_links on delete cascade,
  url             text not null,      -- endereço a conferir (relativo já resolvido para o domínio do portal)
  url_original    text not null,      -- como está no conteúdo
  origem_tabela   text not null,
  origem_id       uuid not null,
  origem_titulo   text,
  verificado      boolean not null default false,
  reservado_ate   timestamptz,        -- lote em conferência por uma execução da função
  status_http     smallint,
  erro            text
);
create index on public.verificacao_fila (verificacao_id, verificado, url);
alter table public.verificacao_fila enable row level security;
revoke all on public.verificacao_fila from anon, authenticated;
grant select, insert, update, delete on public.verificacao_fila to service_role;

-- -------------------------------------------------------------
-- Início: reserva a verificação mais antiga e monta a fila a partir do conteúdo publicado.
-- Links para arquivos do próprio Storage são conferidos aqui mesmo (storage.objects),
-- sem requisição: são milhares e não precisam sair do banco.
-- -------------------------------------------------------------
create or replace function public.verificacao_iniciar()
returns table (verificacao_id uuid, municipio_id uuid, ja_iniciada boolean)
language plpgsql
security definer
set search_path = ''
as $$
#variable_conflict use_column
declare
  v_id      uuid;
  v_mid     uuid;
  v_status  text;
  v_base    text;
  v_storage text;
  v_amb     text := coalesce((select valor from interno.configuracao where chave = 'ambiente'), 'producao');
begin
  -- Retoma a que está em andamento (função caiu ou estourou o tempo); senão, a pendente mais antiga.
  select v.id, v.municipio_id, v.status into v_id, v_mid, v_status
    from public.verificacoes_links v
   where v.status = 'processando' or v.status = 'pendente'
   order by (v.status = 'processando') desc, v.iniciado_em
   limit 1
   for update skip locked;
  if v_id is null then return; end if;

  if v_status = 'processando' then
    update public.verificacoes_links set atualizado_em = now() where id = v_id;
    return query select v_id, v_mid, true;
    return;
  end if;

  select 'https://' || d.dominio into v_base from public.municipio_dominios d
   where d.municipio_id = v_mid and d.principal and d.ambiente::text = v_amb limit 1;
  v_storage := (select valor from interno.configuracao where chave = 'supabase_url') || '/storage/v1/object/public/midias/';

  insert into public.verificacao_fila (verificacao_id, url, url_original, origem_tabela, origem_id, origem_titulo)
  select v_id,
         -- Sem domínio no ambiente, o relativo fica como está e aparece como "endereço inválido".
         case when l.url like '/%' and l.url not like '//%' then coalesce(v_base || l.url, l.url)
              when l.url like '//%' then 'https:' || l.url
              else l.url end,
         l.url, l.tabela, l.id, l.titulo
    from (
      select 'publicacoes' tabela, p.id, p.titulo, (regexp_matches(p.corpo_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1] url
        from public.publicacoes p where p.municipio_id = v_mid and p.status = 'publicado'
      union all
      select 'documentos', d.id, d.titulo, (regexp_matches(d.descricao_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.documentos d where d.municipio_id = v_mid and d.status = 'publicado'
      union all
      select 'documentos', d.id, d.titulo, a.url_externa
        from public.documento_arquivos a join public.documentos d on d.id = a.documento_id
       where d.municipio_id = v_mid and d.status = 'publicado' and a.url_externa is not null
      union all
      select 'paginas', p.id, p.titulo, (regexp_matches(p.corpo_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.paginas p where p.municipio_id = v_mid and p.status = 'publicado'
      union all
      select 'servicos', s.id, s.titulo, (regexp_matches(coalesce(s.etapas_html, '') || coalesce(s.requisitos_html, ''), '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.servicos s where s.municipio_id = v_mid and s.status = 'publicado'
      union all
      select 'servicos', s.id, s.titulo, s.url_externa
        from public.servicos s where s.municipio_id = v_mid and s.status = 'publicado' and s.url_externa is not null
      union all
      select 'eventos', e.id, e.titulo, (regexp_matches(e.descricao_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.eventos e where e.municipio_id = v_mid and e.status = 'publicado'
      union all
      select 'eventos', e.id, e.titulo, e.url_externa
        from public.eventos e where e.municipio_id = v_mid and e.status = 'publicado' and e.url_externa is not null
      union all
      select 'perguntas_frequentes', f.id, f.pergunta, (regexp_matches(f.resposta_html, '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.perguntas_frequentes f where f.municipio_id = v_mid and f.status = 'publicado'
      union all
      select 'orgaos', o.id, o.nome, (regexp_matches(coalesce(o.competencias_html, '') || coalesce(o.responsavel_curriculo_html, ''), '(?:href|src)="([^"#][^"]*)"', 'g'))[1]
        from public.orgaos o where o.municipio_id = v_mid and o.ativo
      union all
      select 'destaques', x.id, x.titulo, x.url
        from public.destaques x where x.municipio_id = v_mid and x.status = 'publicado' and x.url is not null
             and (x.fim_em is null or x.fim_em > now())
      union all
      select 'menu_itens', m.id, m.rotulo, m.url from public.menu_itens m where m.municipio_id = v_mid and m.url is not null
      union all
      select 'transparencia_itens', t.id, t.titulo, t.url from public.transparencia_itens t where t.municipio_id = v_mid and t.ativo and t.url is not null
      union all
      select 'sistemas_externos', s.id, s.nome, s.url from public.sistemas_externos s where s.municipio_id = v_mid and s.ativo and s.url is not null
    ) l
   where l.url ~* '^(https?:|/)' ;

  -- Arquivos do próprio Storage: confere direto no banco.
  update public.verificacao_fila f
     set verificado = true,
         status_http = case when exists (
           select 1 from storage.objects o where o.bucket_id = 'midias' and o.name = substr(f.url, length(v_storage) + 1)
         ) then 200 else 404 end
   where f.verificacao_id = v_id and f.url like v_storage || '%';

  update public.verificacoes_links
     set status = 'processando', atualizado_em = now(),
         total_links = (select count(distinct url) from public.verificacao_fila where verificacao_id = v_id)
   where id = v_id;
  return query select v_id, v_mid, false;
end $$;

-- Próximo lote de endereços distintos ainda não conferidos; reserva por 3 min
-- (outra execução simultânea pega outros).
create or replace function public.verificacao_proximos(p_verificacao uuid, p_limite int default 100)
returns table (url text)
language plpgsql
security definer
set search_path = ''
as $$
#variable_conflict use_column
begin
  return query
  with lote as (
    select distinct f.url from public.verificacao_fila f
     where f.verificacao_id = p_verificacao and not f.verificado
       and (f.reservado_ate is null or f.reservado_ate < now())
     limit p_limite
  ), reservados as (
    update public.verificacao_fila f set reservado_ate = now() + interval '3 minutes'
      from lote where f.verificacao_id = p_verificacao and f.url = lote.url and not f.verificado
    returning f.url
  )
  select distinct r.url from reservados r;
  update public.verificacoes_links set atualizado_em = now() where id = p_verificacao;
end $$;

-- Resultado de um lote: [{url, status_http, erro}]
create or replace function public.verificacao_registrar(p_verificacao uuid, p_resultados jsonb)
returns void
language sql
security definer
set search_path = ''
as $$
  update public.verificacao_fila f
     set verificado = true, status_http = (r->>'status_http')::smallint, erro = r->>'erro', reservado_ate = null
    from jsonb_array_elements(p_resultados) r
   where f.verificacao_id = p_verificacao and f.url = r->>'url';
$$;

-- Fecha a verificação: só vira problema o que é falha de fato (404/410, erro do servidor,
-- endereço que não responde). 401/403/405/429 são bloqueios a robôs, não links quebrados.
create or replace function public.verificacao_concluir(p_verificacao uuid)
returns int
language plpgsql
security definer
set search_path = ''
as $$
declare v_problemas int;
begin
  if exists (select 1 from public.verificacao_fila where verificacao_id = p_verificacao and not verificado) then
    return -1;  -- ainda há links a conferir
  end if;
  insert into public.verificacao_problemas (verificacao_id, tipo, url, status_http, erro, origem_tabela, origem_id, origem_titulo)
  select p_verificacao,
         case when f.status_http in (404, 410) then 'link_quebrado' else 'pagina_indisponivel' end,
         f.url_original, f.status_http, f.erro, f.origem_tabela, f.origem_id, f.origem_titulo
    from public.verificacao_fila f
   where f.verificacao_id = p_verificacao
     and (f.status_http in (404, 410) or f.status_http >= 500 or (f.status_http is null and f.erro is not null));
  get diagnostics v_problemas = row_count;
  update public.verificacoes_links
     set status = 'concluida', concluido_em = now(), atualizado_em = now(), problemas = v_problemas
   where id = p_verificacao;
  delete from public.verificacao_fila where verificacao_id = p_verificacao;
  return v_problemas;
end $$;

revoke all on function public.verificacao_iniciar(), public.verificacao_proximos(uuid, int),
  public.verificacao_registrar(uuid, jsonb), public.verificacao_concluir(uuid) from public, anon, authenticated;
grant execute on function public.verificacao_iniciar(), public.verificacao_proximos(uuid, int),
  public.verificacao_registrar(uuid, jsonb), public.verificacao_concluir(uuid) to service_role;

-- -------------------------------------------------------------
-- Agendamento
-- -------------------------------------------------------------
-- Uma verificação pendente por município ativo (a do painel, se já houver, conta).
create or replace function interno.agendar_verificacoes()
returns void
language sql
security definer
set search_path = ''
as $$
  insert into public.verificacoes_links (municipio_id, status)
  select m.id, 'pendente' from public.municipios m where m.ativo
  on conflict do nothing;
$$;

-- Dispara as Edge Functions que têm trabalho na fila. Sem supabase_url configurado, não faz nada.
create or replace function interno.disparar_rotinas()
returns void
language plpgsql
security definer
set search_path = ''
as $$
declare v_url text := (select valor from interno.configuracao where chave = 'supabase_url');
begin
  if v_url is null then return; end if;
  -- Em andamento, a função retoma de onde parou. Sem batimento por 30 min (falha repetida): desiste;
  -- a verificação semanal seguinte tenta de novo.
  update public.verificacoes_links set status = 'erro', erro = 'interrompida sem batimento por 30 min'
   where status = 'processando' and atualizado_em < now() - interval '30 minutes';
  if exists (select 1 from public.verificacoes_links where status in ('pendente', 'processando')) then
    perform net.http_post(url := v_url || '/functions/v1/verificar-links', body := '{}'::jsonb,
                          headers := '{"Content-Type": "application/json"}'::jsonb, timeout_milliseconds := 1000);
  end if;
end $$;

revoke all on all functions in schema interno from public, anon, authenticated;

do $$
begin
  if exists (select 1 from pg_extension where extname = 'pg_cron') then
    -- Domingo, 3h de Brasília (6h UTC).
    perform cron.schedule('agendar-verificacoes', '0 6 * * 0', 'select interno.agendar_verificacoes()');
    perform cron.schedule('disparar-rotinas', '* * * * *', 'select interno.disparar_rotinas()');
  end if;
end $$;
$mig$]);

-- ######## 0013_exportacao ########
-- =============================================================
-- 0013 · Exportação completa por município (RF19, D-32)
-- O admin pede no painel; a Edge Function exportar gera um ZIP com todos os dados
-- do município em formato aberto (JSON e CSV) e a lista dos arquivos com o endereço
-- de cada um, e guarda no bucket privado "exportacoes" (pasta = municipio_id).
-- O admin baixa por link assinado. Disparo: interno.disparar_rotinas (0012).
-- =============================================================

insert into storage.buckets (id, name, public)
values ('exportacoes', 'exportacoes', false)
on conflict (id) do nothing;

-- Só o admin do município (ou a SECKE) lê o que está na pasta do município.
-- Ninguém grava pela API: quem grava é a Edge Function, com a chave de serviço.
create policy "exportacoes: admin baixa" on storage.objects for select to authenticated
  using (bucket_id = 'exportacoes'
         and (public.is_admin(public.municipio_do_arquivo(name)) or public.is_plataforma()));

-- Uma exportação em andamento por município.
create unique index exportacoes_uma_em_andamento on public.exportacoes (municipio_id)
  where status in ('pendente', 'processando');
alter table public.exportacoes add column atualizado_em timestamptz not null default now();

-- O disparador passa a chamar também a exportação.
create or replace function interno.disparar_rotinas()
returns void
language plpgsql
security definer
set search_path = ''
as $$
declare v_url text := (select valor from interno.configuracao where chave = 'supabase_url');
begin
  if v_url is null then return; end if;
  -- Verificação em andamento: a função retoma de onde parou. Sem batimento por 30 min
  -- (falha repetida): desiste; a verificação semanal seguinte tenta de novo.
  update public.verificacoes_links set status = 'erro', erro = 'interrompida sem batimento por 30 min'
   where status = 'processando' and atualizado_em < now() - interval '30 minutes';
  if exists (select 1 from public.verificacoes_links where status in ('pendente', 'processando')) then
    perform net.http_post(url := v_url || '/functions/v1/verificar-links', body := '{}'::jsonb,
                          headers := '{"Content-Type": "application/json"}'::jsonb, timeout_milliseconds := 1000);
  end if;

  -- Exportação parada há 15 min (a função leva poucos minutos): volta para a fila uma vez;
  -- se já foi retomada, vira erro (o admin pode pedir de novo).
  update public.exportacoes
     set status = case when erro is null then 'pendente' else 'erro' end,
         erro = coalesce(erro, 'retomada após interrupção'), atualizado_em = now()
   where status = 'processando' and atualizado_em < now() - interval '15 minutes';
  if exists (select 1 from public.exportacoes where status = 'pendente') then
    perform net.http_post(url := v_url || '/functions/v1/exportar', body := '{}'::jsonb,
                          headers := '{"Content-Type": "application/json"}'::jsonb, timeout_milliseconds := 1000);
  end if;
end $$;

revoke all on all functions in schema interno from public, anon, authenticated;

insert into supabase_migrations.schema_migrations (version, name, statements)
values ('20261012000013', '0013_exportacao', array[$mig$-- =============================================================
-- 0013 · Exportação completa por município (RF19, D-32)
-- O admin pede no painel; a Edge Function exportar gera um ZIP com todos os dados
-- do município em formato aberto (JSON e CSV) e a lista dos arquivos com o endereço
-- de cada um, e guarda no bucket privado "exportacoes" (pasta = municipio_id).
-- O admin baixa por link assinado. Disparo: interno.disparar_rotinas (0012).
-- =============================================================

insert into storage.buckets (id, name, public)
values ('exportacoes', 'exportacoes', false)
on conflict (id) do nothing;

-- Só o admin do município (ou a SECKE) lê o que está na pasta do município.
-- Ninguém grava pela API: quem grava é a Edge Function, com a chave de serviço.
create policy "exportacoes: admin baixa" on storage.objects for select to authenticated
  using (bucket_id = 'exportacoes'
         and (public.is_admin(public.municipio_do_arquivo(name)) or public.is_plataforma()));

-- Uma exportação em andamento por município.
create unique index exportacoes_uma_em_andamento on public.exportacoes (municipio_id)
  where status in ('pendente', 'processando');
alter table public.exportacoes add column atualizado_em timestamptz not null default now();

-- O disparador passa a chamar também a exportação.
create or replace function interno.disparar_rotinas()
returns void
language plpgsql
security definer
set search_path = ''
as $$
declare v_url text := (select valor from interno.configuracao where chave = 'supabase_url');
begin
  if v_url is null then return; end if;
  -- Verificação em andamento: a função retoma de onde parou. Sem batimento por 30 min
  -- (falha repetida): desiste; a verificação semanal seguinte tenta de novo.
  update public.verificacoes_links set status = 'erro', erro = 'interrompida sem batimento por 30 min'
   where status = 'processando' and atualizado_em < now() - interval '30 minutes';
  if exists (select 1 from public.verificacoes_links where status in ('pendente', 'processando')) then
    perform net.http_post(url := v_url || '/functions/v1/verificar-links', body := '{}'::jsonb,
                          headers := '{"Content-Type": "application/json"}'::jsonb, timeout_milliseconds := 1000);
  end if;

  -- Exportação parada há 15 min (a função leva poucos minutos): volta para a fila uma vez;
  -- se já foi retomada, vira erro (o admin pode pedir de novo).
  update public.exportacoes
     set status = case when erro is null then 'pendente' else 'erro' end,
         erro = coalesce(erro, 'retomada após interrupção'), atualizado_em = now()
   where status = 'processando' and atualizado_em < now() - interval '15 minutes';
  if exists (select 1 from public.exportacoes where status = 'pendente') then
    perform net.http_post(url := v_url || '/functions/v1/exportar', body := '{}'::jsonb,
                          headers := '{"Content-Type": "application/json"}'::jsonb, timeout_milliseconds := 1000);
  end if;
end $$;

revoke all on all functions in schema interno from public, anon, authenticated;
$mig$]);

-- ######## 0014_verificacao_concluir_trava ########
-- =============================================================
-- 0014 · Verificação de links: conclusão uma vez só (D-31)
-- No primeiro teste, duas execuções da Edge Function terminaram juntas e as duas
-- gravaram os problemas (434 registros para 217 problemas). Agora a conclusão trava
-- a verificação (FOR UPDATE): a segunda espera a primeira e vê que já está concluída.
-- =============================================================

create or replace function public.verificacao_concluir(p_verificacao uuid)
returns int
language plpgsql
security definer
set search_path = ''
as $$
declare v_problemas int;
begin
  perform 1 from public.verificacoes_links where id = p_verificacao and status = 'processando' for update;
  if not found then
    return coalesce((select problemas from public.verificacoes_links where id = p_verificacao), 0);
  end if;
  if exists (select 1 from public.verificacao_fila where verificacao_id = p_verificacao and not verificado) then
    return -1;  -- ainda há links a conferir
  end if;
  insert into public.verificacao_problemas (verificacao_id, tipo, url, status_http, erro, origem_tabela, origem_id, origem_titulo)
  select p_verificacao,
         case when f.status_http in (404, 410) then 'link_quebrado' else 'pagina_indisponivel' end,
         f.url_original, f.status_http, f.erro, f.origem_tabela, f.origem_id, f.origem_titulo
    from public.verificacao_fila f
   where f.verificacao_id = p_verificacao
     and (f.status_http in (404, 410) or f.status_http >= 500 or (f.status_http is null and f.erro is not null));
  get diagnostics v_problemas = row_count;
  update public.verificacoes_links
     set status = 'concluida', concluido_em = now(), atualizado_em = now(), problemas = v_problemas
   where id = p_verificacao;
  delete from public.verificacao_fila where verificacao_id = p_verificacao;
  return v_problemas;
end $$;

revoke all on function public.verificacao_concluir(uuid) from public, anon, authenticated;
grant execute on function public.verificacao_concluir(uuid) to service_role;

insert into supabase_migrations.schema_migrations (version, name, statements)
values ('20261012000014', '0014_verificacao_concluir_trava', array[$mig$-- =============================================================
-- 0014 · Verificação de links: conclusão uma vez só (D-31)
-- No primeiro teste, duas execuções da Edge Function terminaram juntas e as duas
-- gravaram os problemas (434 registros para 217 problemas). Agora a conclusão trava
-- a verificação (FOR UPDATE): a segunda espera a primeira e vê que já está concluída.
-- =============================================================

create or replace function public.verificacao_concluir(p_verificacao uuid)
returns int
language plpgsql
security definer
set search_path = ''
as $$
declare v_problemas int;
begin
  perform 1 from public.verificacoes_links where id = p_verificacao and status = 'processando' for update;
  if not found then
    return coalesce((select problemas from public.verificacoes_links where id = p_verificacao), 0);
  end if;
  if exists (select 1 from public.verificacao_fila where verificacao_id = p_verificacao and not verificado) then
    return -1;  -- ainda há links a conferir
  end if;
  insert into public.verificacao_problemas (verificacao_id, tipo, url, status_http, erro, origem_tabela, origem_id, origem_titulo)
  select p_verificacao,
         case when f.status_http in (404, 410) then 'link_quebrado' else 'pagina_indisponivel' end,
         f.url_original, f.status_http, f.erro, f.origem_tabela, f.origem_id, f.origem_titulo
    from public.verificacao_fila f
   where f.verificacao_id = p_verificacao
     and (f.status_http in (404, 410) or f.status_http >= 500 or (f.status_http is null and f.erro is not null));
  get diagnostics v_problemas = row_count;
  update public.verificacoes_links
     set status = 'concluida', concluido_em = now(), atualizado_em = now(), problemas = v_problemas
   where id = p_verificacao;
  delete from public.verificacao_fila where verificacao_id = p_verificacao;
  return v_problemas;
end $$;

revoke all on function public.verificacao_concluir(uuid) from public, anon, authenticated;
grant execute on function public.verificacao_concluir(uuid) to service_role;
$mig$]);

-- ######## pg_net fora do schema public (aviso do verificador de segurança) ########
-- A 0011 criou a extensão sem schema. As funções dela ficam no schema "net"
-- (net.http_post), que não muda; só o registro da extensão sai de public.
drop extension if exists pg_net;
create extension pg_net with schema extensions;

commit;

-- Conferência (deve listar 0011 a 0020 e os jobs do pg_cron):
select name from supabase_migrations.schema_migrations order by version;
select jobname, schedule from cron.job;
