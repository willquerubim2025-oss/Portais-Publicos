# Portal Educação Paulínia — Arquivo de Contexto

Oct 10, 2026 · @William Mateus

Complemento da Especificação do Brainstorm: explica o porquê das decisões e como trabalhar no projeto.

## 1. Quem, por quê e para quem

**Quem constrói.** Secke Sistemas (Secke – Tecnologias e Sistemas), empresa de William Matheus, especializada em sistemas para o setor público brasileiro. A Secke nasceu da frustração de servidores de carreira com sistemas e atendimento de fornecedores ao governo; a missão é levar ao setor público qualidade e atendimento de nível privado. William também é servidor da SMEDU de Paulínia, o que lhe dá conhecimento direto das dores da Secretaria.

**Para quem.** Secretaria Municipal de Educação de Paulínia/SP. A proposta será apresentada à Secretária de Educação. A SMEDU não tem portal algum hoje, o que fortalece a justificativa.

**Por quê.** Informações e serviços da educação estão espalhados ou não existem online; a comunicação formal interna é toda em papel; pais e estudantes precisam ligar ou ir até a Secretaria para resolver coisas simples.

**Estratégia maior.** Este é o primeiro de uma série de portais públicos (meta: ao menos 10 no ar). Por isso a base é o projeto Supabase Portal Municipal, multiórgão. Tudo que for construído deve servir a outros órgãos e municípios: nada de regra específica de Paulínia cravada no código — o que é específico vira dado/configuração do órgão.

**Natureza do piloto.** É uma peça de convencimento. A primeira impressão da Secretária decide o projeto. Prioridade máxima: acabamento visual, conteúdo real e sensação de produto pronto. Funcionalidades complexas (satélites) aparecem como botões "em breve", mostrando visão sem atrasar a entrega.

## 2. O raciocínio por trás das decisões

**Largura total e cores alternadas.** William rejeitou explicitamente o layout centralizado com margens laterais vazias, comum em sites de prefeitura, por parecer datado e sem presença. As seções de ponta a ponta com tons alternados dão ritmo e sensação de produto moderno.

**Hero baixo, não tela cheia.** O destaque precisa impactar, mas sem empurrar as notícias para baixo da dobra. O visitante deve ver destaque e notícias ao abrir. Por isso, cerca de metade da altura da tela.

**Carrossel lento.** Transição rápida parece anúncio e cansa; lenta transmite calma institucional e dá tempo de ler a mensagem.

**Cards que saltam, com freio.** William quer que avisos importantes se imponham. O risco é virar pop-up irritante, que as pessoas fecham sem ler. Daqui vieram as regras de frequência (uma vez por visitante), prioridade e validade automática.

**Paleta da Prefeitura + cores próprias.** O visitante chega pelo site da Prefeitura; se o portal parecer de outro lugar, gera desconfiança ("será que é oficial?"). Ao mesmo tempo, William quer identidade própria da Educação. Solução: cores institucionais nos elementos estruturais, cores vivas nas seções, layout próprio.

**Inspiração, não cópia.** William pediu para "copiar" bons modelos. A leitura combinada: estudar e adotar as boas soluções de estrutura e experiência, com visual próprio. Cópia literal ficaria genérica e poderia gerar problema de direito autoral.

**Avatares em vez de foto de banco.** Foto de desconhecido ao lado do nome real da Secretária confundiria quem assiste à demonstração. Avatar neutro deixa claro que a foto oficial entra depois. Foi uma sugestão, ainda a confirmar com William; banco de imagem continua opção se ele preferir.

**RBAC configurável, com trava no servidor.** William quer que o administrador ligue e desligue cada funcionalidade por papel. Isso só é confiável se: (a) o catálogo de permissões vier do código, senão fica desatualizado; (b) o bloqueio for no banco (RLS), senão é cosmético; (c) houver escopo, porque o diretor só deve agir sobre sua escola. Todas as salvaguardas sugeridas (master protegido, múltiplos papéis, histórico, papéis novos pelo painel) foram aprovadas por William.

**Satélites separados.** Cada sistema (Área do Estudante, CI, etc.) é grande o suficiente para ser um projeto. Mantê-los fora da fase 1 garante entrega rápida e bonita do portal; os botões "em breve" mostram a visão completa à Secretária.

**CI eletrônica como transição ao SEI.** A Prefeitura pretende adotar o SEI, mas William avalia que vai demorar muito. Posicionar a CI como solução de transição (desativável ou ampliável) evita conflito político e aproveita o intervalo.

**Conteúdo real.** Demonstração com lorem ipsum não convence. Notícias verdadeiras, hierarquizadas por importância, fazem o portal parecer vivo desde o primeiro dia.

## 3. Instruções de trabalho para o Claude Code

1. **Leia antes de construir.** Inspecione o projeto Supabase Portal Municipal (`qgywucdnaeheqndcxtho`): tabelas com colunas, chaves, políticas RLS, funções, triggers e migrações. Entenda como `municipios`, `orgaos`, `membros`, `perfis` e `equipe_plataforma` fazem o isolamento antes de propor qualquer mudança.
2. **Verifique o repositório existente.** O projeto já prevê a parte administrativa. Identifique o que existe de frontend/admin e reutilize.
3. **Migrações aditivas e seguras.** Nada de apagar ou renomear o que existe sem confirmação de William. Toda tabela nova referencia o órgão/município e nasce com RLS no padrão existente. Apresente o plano de migração antes de aplicar.
4. **Permissão primeiro.** Ao criar qualquer funcionalidade, declare seu código de permissão no registro central e proteja-a no servidor. Nada é "só visual".
5. **Configuração, não código.** Nomes, cores, textos, cards, slides, rodapé e botões de satélites vêm do banco, editáveis pelo painel. Paulínia é o primeiro órgão, não o único.
6. **Fase 1 apenas.** Não implemente Área do Estudante, CI Eletrônica nem Ouvidoria completa. Crie apenas os registros e botões "em breve".
7. **Padrão visual alto.** Antes de entregar uma tela, compare com os melhores portais públicos e privados. Se não parecer produto profissional, refine. Teste em celular.
8. **Conteúdo real e legal.** Ao montar a carga inicial, use fontes oficiais da Prefeitura; reescreva notícias de jornais com link para a fonte; não copie fotos de veículos privados; revise fotos com alunos.
9. **Não invente dados oficiais.** Endereço, telefone, nomes e cargos da equipe: use o que William fornecer; enquanto isso, marque como pendente no painel.
10. **Stack.** Stack padrão de William: React + TypeScript + Vite; Supabase (PostgreSQL, RLS, Edge Functions, Storage); Claude API para IA (ex.: transcrição/classificação); Cloudflare Workers para proxy de API; hospedagem na Hostinger por deploy manual em ZIP. Mantenha o que o repositório já usa. Não criar novo projeto Supabase (custo por projeto): tudo dentro do Portal Municipal. Estilo de entrega: mudanças cirúrgicas, sem alterar o que não foi pedido; arquivos completos em vez de trechos; validar antes de entregar (ex.: npx tsc --noEmit).

**Ordem sugerida de execução:**

1. Diagnóstico do banco e do repositório; relatório do que existe vs. o que falta.
2. Plano de migração (permissões, unidades, equipe gestora, avisos, prioridade).
3. Sistema de permissões (registro no código, sincronização, RLS, painel).
4. Paleta, tipografia e componentes base (botões e cards vivos).
5. Página inicial seção por seção.
6. Painel administrativo de conteúdo.
7. Carga inicial de conteúdo real.
8. Revisão de acessibilidade, desempenho e mobile.

## 4. Glossário e referências

| Termo | Significado |
| --- | --- |
| SMEDU | Secretaria Municipal de Educação de Paulínia |
| CI | Comunicação Interna — documento oficial entre setores; hoje em papel, numerado por setor/ano (ex.: CI 157/VSV/2026) |
| SEI | Sistema Eletrônico de Informações — processo eletrônico que a Prefeitura pretende adotar |
| Supervisor escolar | Profissional da SMEDU que acompanha um conjunto de escolas |
| Diretor (papel) | Diretor de escola, administrador regional da sua unidade |
| Diretor de divisão | Gestor de departamento/divisão da SMEDU (3º nível da Equipe Gestora) |
| PROEB | Programa de escolas conveniadas de educação infantil de Paulínia |
| Bolsa Educação / Bolsa + | Programa municipal de bolsas e o sistema de gestão feito por William |
| SIMAPE Escolar | Sistema Municipal de Planejamento Escolar (mapa e alocação escolar) feito por William |
| PNTP | Programa Nacional de Transparência Pública — critérios já carregados no banco |
| RLS | Row Level Security do Postgres/Supabase — isolamento e permissão por linha |
| Satélite | Sistema à parte, acessado por botão no portal |

**Bases legais citadas:** Lei 13.460/2017 (usuário do serviço público / ouvidoria); Lei 14.063/2020 (assinaturas eletrônicas no setor público); LGPD (Lei 13.709/2018); ECA (Lei 8.069/1990); Lei Brasileira de Inclusão (Lei 13.146/2015) e eMAG (acessibilidade); Lei 9.610/1998 (direitos autorais).

**Referências de portais de secretaria de educação:** Curitiba e Campinas (modelo de subdomínio próprio).
