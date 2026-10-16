# Roteiro para concluir o Portal Educação (fase 1)

Situação em 16/10/2026. Lista do que falta para o portal da SMEDU ir ao ar, com atenção especial ao acesso dos servidores e aos sistemas que orbitam o portal. Os detalhes técnicos ficam em `portal-municipal/docs/07-pendencias.md` e `11-checklist-ir-ao-ar.md`; o que depende da Secretaria, em `docs/reuniao/smedu-pendencias.md`.

## 1. Acesso dos servidores e sistemas em órbita

### O que já existe
| Peça | Situação |
|---|---|
| **Login único** (Supabase Auth) | Pronto. Um e-mail e uma senha por pessoa, valendo para o painel. A mesma conta pode servir a mais de uma organização. |
| **Papéis configuráveis** (D-38, D-77, D-78) | Prontos na homologação e na produção. Papéis de sistema: Administrador, Diretor, Professor e Estudante; a Secretaria pode criar outros pelo painel (ex.: Redator, Coordenador pedagógico). |
| **Permissões com chave liga/desliga** | Prontas: 8 permissões hoje (conteúdo, publicação, administração, usuários, papéis, unidades, equipe). Novas funções declaram a sua no código e aparecem desligadas no painel. A trava está no banco (RLS), não só na tela. |
| **Escopo** (rede, região, unidade) | Pronto no banco e na tela de Vínculos. Ex.: um diretor com `unidades.editar` só na própria escola. |
| **Mais de um papel por pessoa** | Pronto (ex.: diretor que também é professor). |
| **Convite de servidor** | Pronto: Vínculos → "Dar papel a alguém". Sem SMTP, o convite gera um link para repassar (o e-mail ainda não é enviado). |
| **Histórico de permissões e auditoria** | Pronto: quem mudou o quê, quando, de → para. |
| **Desligar o acesso de quem sai** | Pronto: o vínculo é desativado; a conta e o histórico ficam. |
| **Cadastro de sistemas externos** (`sistemas_externos`, D-07) | Pronto: nome, fornecedor, categoria, endereço, ativo. Hoje são usados como **link** em itens da Transparência e em cards de Serviços. |
| **Cards "Em breve"** | Prontos: um card de serviço pode ficar "Em breve" e ser ligado depois, sem código. |

### O que falta
1. ~~**Entrada do servidor no portal.**~~ Feito em 16/10/2026 (D-94): link "Acesso do servidor" no rodapé.
2. ~~**Central de ferramentas do servidor no painel**~~ Feito em 16/10/2026 (D-94, migração 0025): "Meus sistemas" na tela inicial do painel; cadastro em Transparência → Sistemas, com "Para quem" e os papéis. Texto original da proposta: A tela inicial do painel ainda não lista os sistemas que cada servidor usa. Proposta: uma página "Meus sistemas" com os `sistemas_externos` marcados como internos, filtrados pelo papel (ex.: o diretor vê o SIMAPE e o sistema de matrícula; a Divisão de Bolsas vê o Bolsa +). Precisa de: uma coluna de público (público geral ou servidores) e a permissão de cada sistema (`sistemas.<nome>.acessar`) no catálogo.
3. **Login único com os sistemas satélites.** Hoje cada sistema externo tem login próprio. Caminhos, do mais simples ao mais completo:
   - **Sistemas de terceiros da Prefeitura** (Fiorilli, SISS, Fala.BR, SEI): continuam só por link (D-07). Não há como compartilhar o login sem integração do fornecedor.
   - **Satélites novos da Secke** (Área do Estudante, CI Eletrônica, Ouvidoria própria): construir **no mesmo projeto Supabase**. Assim usam a mesma conta, os mesmos papéis e as mesmas permissões, sem login novo.
   - **Sistemas que William já tem** (Bolsa +, SIMAPE Escolar, apoio à recepção): estão em outros projetos. Opções: migrar para o mesmo projeto, ou login federado (o portal como provedor de identidade, por OAuth/OpenID). Decisão a tomar sistema por sistema, depois de levantar como cada um faz login hoje.
4. **Papéis Professor e Estudante sem função ainda.** Existem, mas não têm permissão nenhuma: só passam a fazer sentido com a Área do Estudante. Para estudantes (menores de idade): login institucional, moderação e LGPD/ECA antes de abrir.
5. **E-mail do sistema (SMTP).** Sem ele, convites e "esqueci minha senha" não chegam por e-mail. Obrigatório antes de convidar os servidores de verdade.
6. **Primeiro administrador da SMEDU** (item 11 das pendências da SMEDU) e treinamento dos servidores.
7. **Levantamento com a Secretaria** (novo item 18 de `smedu-pendencias.md`): quais sistemas os servidores usam hoje, quem usa cada um, como fazem login e se há e-mail institucional para todos.

## 2. O que depende de William agora
- Rodar as migrações **0024** e **0025** no SQL Editor (homologação e produção). Depois, a Secke publica painel e portal.

## 3. Técnico, sem depender da Secretaria
- **Antes de ir ao ar (obrigatório):**
  - Cloudflare Workers Paid (US$ 5/mês) e decidir a conta da produção;
  - **testar o isolamento do cache entre organizações** com dois domínios (a SMEDU é a 2ª organização);
  - SMTP próprio nos dois projetos Supabase;
  - painel e portal de **produção** publicados, endereços no login da produção;
  - ~~backup extra do banco no R2 com teste de restauração~~ (rodando todo dia desde 05/10); ~~cópia dos arquivos para o R2~~ (configurada e verde em 16/10, D-96); monitoramento de disponibilidade (UptimeRobot, conta do William);
  - ~~Security e Performance Advisors da produção revisados~~ (16/10, nada urgente; repetir antes da troca de domínio);
  - adaptar os testes automáticos do painel (`npm run e2e`) para a SMEDU (hoje usam Jeriquara);
  - apagar o conteúdo fictício e os usuários de teste (`admin.teste`, `redator.teste`).
- **Qualidade:** teste com leitor de tela (NVDA); ~~Core Web Vitals no celular~~ e ~~checklist de SEO~~ (medidos na homologação em 16/10, D-95; repetir na produção); ~~**VLibras**~~ (instalado em 16/10/2026, D-94; conferir no navegador).
- **Produto:** pacote padrão para câmara e autarquia (D-90); ~~importação de redirecionamentos em lote~~ (D-95); ~~cópia dos arquivos do Storage para o R2~~ (D-96, configurada); notícias das escolas com escopo por unidade (permissões, fase 1C).

## 4. Depende da Secretaria
Ver `docs/reuniao/smedu-pendencias.md` (18 itens). Os que bloqueiam ir ao ar: supervisores por escola, Matrícula 2027 confirmada, equipe gestora real, páginas legais confirmadas, autorização de imagens, domínio/IBGE/CNPJ/primeiro administrador, agenda real.

## 5. Fases futuras (fora da fase 1)
Área do Estudante completa (conteúdo, reforço, dúvidas com professores), CI Eletrônica, Ouvidoria própria com áudio e protocolo, integrações com Bolsa +, SIMAPE e apoio à recepção.
