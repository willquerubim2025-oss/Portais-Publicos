# Portal Educação Paulínia — Especificação do Brainstorm

Oct 10, 2026 · @William Mateus

## 1. Visão geral

O Portal Educação Paulínia é o portal próprio da Secretaria Municipal de Educação (SMEDU) de Paulínia/SP, acessado por um link no site oficial da Prefeitura. Hoje a SMEDU não tem site nem portal algum.

**Objetivo.** Centralizar todas as informações e serviços da Secretaria num só lugar, para a população, estudantes, professores, diretores e equipe interna.

**Papel de convencimento.** A versão piloto será apresentada à Secretária de Educação. Ela precisa causar uma impressão muito positiva à primeira vista: profissional, moderna, bonita, confiável. Isso é requisito, não detalhe.

**Modelo replicável.** O portal é o primeiro de uma série (meta: ao menos 10 portais públicos no ar), construído sobre uma base multiórgão no Supabase (projeto Portal Municipal).

**Públicos.**

- População / pais e responsáveis (matrícula, contato com a escola, ouvidoria, notícias)
- Estudantes (orientação, estudo, reforço, interação com professores)
- Professores e diretores de escola
- Equipe da SMEDU (administração, comunicação interna)
- Imprensa e órgãos de controle (transparência, números)

## 2. Princípios de design e identidade visual

O portal deve ser deslumbrante, com design próprio, mas em comunicação visual clara com o site institucional da Prefeitura.

**Layout de largura total.**

- Nada de site centralizado com faixas laterais vazias. Todas as seções ocupam a largura inteira da tela.
- As seções alternam cores, tons e subtons ao longo da rolagem, criando ritmo visual.

**Paleta.**

- Cores predominantes = as mesmas do site institucional da Prefeitura de Paulínia, nos elementos principais (cabeçalho, rodapé, botões de ação, títulos). Extrair os códigos exatos do site oficial.
- Cores complementares mais vivas e dinâmicas nas seções e áreas temáticas, derivadas da base (3 a 4 variações), para marcar que é o portal de uma secretaria específica.
- Variado sem virar carnaval; todas as combinações testadas em contraste (acessibilidade).
- Layout, cards, tipografia e composição próprios: não imitar a estrutura do site da Prefeitura. Sensação desejada: mesma família, casa própria.

**Acabamento.**

- Tipografia moderna e legível; títulos fortes, textos confortáveis.
- Fotos reais, grandes, bem recortadas. Nada de lorem ipsum.
- Muito respiro em branco; aparência institucional sem peso.
- Movimento elegante: elementos que surgem suavemente na rolagem, sem exagero.
- Cards e botões inspirados nos melhores portais (estrutura e experiência), com visual próprio de Paulínia. Inspiração, não cópia.

**Botões e cards vivos.** Cuidado especial com o dinamismo: reação à passagem do mouse (leve elevação, mudança de cor, sombra, ícone que se mexe) e resposta ao toque no celular.

**Celular em primeiro lugar.** A maioria dos pais abrirá pelo telefone, inclusive por link no WhatsApp.

**Rápido.** Portal bonito e lento perde a primeira impressão: imagens otimizadas, carregamento progressivo.

## 3. Estrutura da página inicial

Ordem sugerida de cima para baixo: cabeçalho, carrossel de destaque, notícias, serviços, demais seções, equipe gestora, rodapé. Os avisos urgentes sobrepõem tudo.

### 3.1 Entrada

- Link no site oficial da Prefeitura leva ao portal.
- Endereço sugerido: subdomínio `educacao.paulinia.sp.gov.br` (referências: Curitiba, Campinas).
- Botão de volta ao site da Prefeitura, para o portal não parecer solto.

### 3.2 Cabeçalho

- Brasão da Prefeitura de Paulínia + texto "Secretaria Municipal de Educação".
- Menu de navegação e acesso ao login.

### 3.3 Destaque (hero) em carrossel

- Faixa de largura total, altura contida (cerca de metade da tela), deixando notícias visíveis sem rolar.
- Imagens bonitas ou mensagens de campanhas (matrícula aberta, volta às aulas, eventos).
- Três slides de início, cada um com imagem e mensagem próprias e botão de ação opcional ("Saiba mais", "Faça a matrícula").
- Transição lenta e suave (esmaecimento), cerca de 7 a 8 segundos por slide.
- Indicadores de posição; pausa com o mouse em cima; respeitar `prefers-reduced-motion`.

### 3.4 Notícias

- Logo abaixo do destaque. Carrossel ou grade: manchete principal maior, demais menores ao lado, sempre com foto.
- Recebem as notícias secundárias (ver seção 4).

### 3.5 Área de Serviços (cards de acesso rápido)

Cards grandes e clicáveis para os serviços mais procurados. Cada card: ícone, título curto, uma linha de descrição, status ativo ou "em breve", ordem definida pelo administrador. Lista aberta: novos cards serão somados.

| # | Card | Comportamento |
| --- | --- | --- |
| 1 | Matrícula Escolar | Informações e acesso ao processo de matrícula |
| 2 | Área do Estudante | Leva ao sistema satélite (seção 7.1); inativo na fase 1 |
| 3 | Secretaria de Educação / Organograma | Estrutura da Secretaria; pode levar à seção Equipe Gestora |
| 4 | Educação Municipal em Números | Indicadores da rede (escolas, alunos, vagas, IDEB etc.) |
| 5 | Fale com o supervisor escolar da escola do seu filho | Busca pela escola (nome ou bairro) e mostra o supervisor responsável e o canal de contato |
| 6 | Ouvidoria | Manifestação por áudio (transcrito) ou texto (seção 7.3) |

### 3.6 Seções temáticas

Seções de largura total com cores alternadas (conteúdo a definir: eventos, programas, escolas, transparência, perguntas frequentes etc.).

### 3.7 Equipe Gestora

Seção única com design que mostra a hierarquia em três níveis:

1. Secretária e Secretária Adjunta — cards maiores, no topo.
2. Supervisores — cards médios.
3. Diretores de divisão/departamento — cards menores, agrupados por divisão. (Chefes de divisão não entram.)

- Cada card: foto, nome, cargo, contato institucional opcional.
- Depende de autorização das pessoas e da Secretária: o administrador pode ocultar qualquer card ou a seção inteira.
- Piloto: nomes e cargos reais (fornecidos por William no momento oportuno); fotos provisórias como avatares neutros (silhueta estilizada ou iniciais sobre a cor do portal). Banco de imagem só se William preferir. Nunca usar fotos reais sem autorização.

### 3.8 Rodapé

- Dados da SMEDU: localização no Paço Municipal, endereço completo, telefone.
- Acréscimos: horário de atendimento, link para o site da Prefeitura, atalhos para Ouvidoria e Transparência, recursos de acessibilidade.
- Dados exatos confirmados com William antes de irem ao ar.

### 3.9 Cards de aviso (comunicados que saltam na tela)

Informações muito importantes aparecem sobre todo o conteúdo (ex.: período de matrícula, suspensão de aulas, prazos do Bolsa Educação).

- Níveis de prioridade: urgente em modal; informativo como faixa discreta no topo.
- Aparece uma vez por visitante (não a cada página); botão claro de fechar.
- Data de início e fim: somem sozinhos.
- Acessível por teclado e leitor de tela.

## 4. Conteúdo

O piloto vai ao ar com conteúdo real sobre a SMEDU, organizado por grau de importância.

### 4.1 Carga inicial

Na primeira montagem está autorizado, dentro dos limites legais, buscar informações, fotos e notícias sobre a Secretaria de Educação no site da Prefeitura, em jornais e em publicações. O portal deve explorar toda a sua potencialidade visual com notícias verdadeiras.

### 4.2 Hierarquia por importância

Cada conteúdo recebe um grau de relevância que define onde aparece. No sistema: campo de prioridade na publicação; o administrador pode promover ou rebaixar qualquer item.

| Grau | Onde aparece | Exemplo |
| --- | --- | --- |
| Urgente / interesse geral imediato | Card que salta na tela, sobre tudo | Suspensão de aulas, prazo final de matrícula |
| Principal do momento | Slide do carrossel de destaque | Campanha de matrícula, grande evento |
| Secundária | Seção de notícias, com foto | Evento em escola, entrega de obra |
| Permanente | Cards de serviço e páginas institucionais | Matrícula, organograma, ouvidoria |

### 4.3 Limites legais da carga inicial

- Conteúdo da própria Prefeitura: pode ser reaproveitado (publicação oficial do mesmo ente), mantendo data e crédito.
- Jornais e veículos privados: texto e fotos têm direito autoral. Reescrever a informação com palavras próprias e linkar a matéria original; nunca copiar texto nem foto.
- Fotos com alunos: só as já publicadas oficialmente pela Prefeitura, revisadas antes de ir ao ar (proteção de imagem de crianças e adolescentes, ECA).
- Fotos de pessoas da equipe gestora: não usar sem autorização (ver 3.7).

## 5. Papéis e permissões configuráveis (RBAC)

O painel administrativo permite escolher, papel por papel, o que cada um pode ou não fazer, com uma chave liga/desliga por funcionalidade. Isso precisa estar amarrado no banco de dados e no código.

### 5.1 Papéis

| Papel | Quem é | Alcance |
| --- | --- | --- |
| Desenvolvedor (master) | Secke Sistemas | Tudo, inclusive configurações técnicas |
| Administrador | Equipe da SMEDU | Toda a rede |
| Diretor | Diretores de escola (administradores regionais) | Sua(s) unidade(s) / região |
| Professor | Professores da rede | Suas turmas e conteúdos |
| Estudante | Alunos | Seus próprios dados e conteúdos |

### 5.2 Painel de permissões

O administrador seleciona um papel (ex.: Professor) e vê a lista de todas as funcionalidades do sistema, separadas e classificadas por módulo (Notícias, Comunicados, Serviços, Equipe, Área do Estudante, Conteúdos, Dúvidas, Usuários...), cada uma com sua chave de ativar/desativar e, quando aplicável, o escopo.

### 5.3 Regras de implementação (obrigatórias)

1. Toda funcionalidade nasce com um código de permissão (ex.: `noticias.publicar`, `avisos.criar`, `conteudos.aprovar`, `duvidas.responder`). Nenhuma tela, botão, rota ou ação existe sem declarar a sua.
2. O catálogo é gerado a partir do código: os arquivos do sistema registram as permissões e elas sincronizam com o banco automaticamente. Funcionalidade nova aparece sozinha no painel, desligada por padrão.
3. A trava fica no servidor, não só na tela: esconder o botão é conforto; o bloqueio real é no banco (políticas RLS do Supabase consultando a tabela de permissões) e nas funções de servidor.
4. Permissão tem escopo, além de sim/não: rede inteira, região, unidade ou próprio (ex.: diretor edita notícias só da sua escola).
5. O papel master não aparece para edição e não pode ser desligado: ninguém tranca a Secke para fora.
6. Um usuário pode ter mais de um papel (ex.: diretor que também dá aula).
7. Histórico de toda mudança de permissão: quem, quando, papel, permissão, de → para.
8. Criação de papéis novos pelo painel (coordenador pedagógico, secretário de escola, nutricionista), sem mexer em código.

### 5.4 Esqueleto de dados proposto

A encaixar na estrutura existente (seção 8); nomes indicativos.

```
papeis            (id, orgao_id, nome, descricao, sistema)
permissoes        (codigo, modulo, nome, descricao, tem_escopo)
papel_permissoes  (papel_id, permissao_codigo, ativo, escopo)
usuario_papeis    (usuario_id, papel_id, unidade_id | regiao_id)
log_permissoes    (quem, quando, papel_id, permissao_codigo, de, para)
```

## 6. Arquitetura: portal no centro, sistemas em órbita

A fase 1 constrói apenas o portal. Os demais sistemas são projetos à parte, mas seus botões de acesso já existem no portal desde o início, inativos ou marcados "em breve", e são ligados pelo administrador quando cada sistema ficar pronto.

- **Portal (fase 1):** página pública, notícias, destaques, avisos, serviços, equipe gestora, transparência, painel administrativo de conteúdo e permissões.
- **Painel do administrador como central de ferramentas:** atalhos para as ferramentas que a SMEDU já usa ou precisa ter (hoje mal desenvolvidas ou inexistentes).
- **Sistemas satélites (fases futuras):**
  - Área do Estudante (7.1)
  - CI Eletrônica / comunicação interna (7.2)
  - Ouvidoria (7.3) — pode começar simples dentro do portal ou ser satélite
  - Sistemas já existentes de William: Bolsa + (gestão do Programa Bolsa Educação), SIMAPE Escolar (planejamento e mapa escolar), apoio à recepção (encaminhamento com alerta em tempo real)
- **Registro dos satélites:** tabela `sistemas_externos` do projeto Portal Municipal (já existe, com 5 registros).
- **Login:** idealmente uma identidade única (Supabase Auth) compartilhada entre portal e satélites, com os papéis da seção 5 valendo em todos.

## 7. Sistemas satélites (registrados para fases futuras)

Estas ideias fazem parte da proposta original, mas não entram na construção da fase 1 além dos botões de acesso.

### 7.1 Área do Estudante

**Orientação e futuro:** vestibulares, vestibulinhos (ETEC, institutos federais), universidades, bolsas, cursos técnicos e gratuitos; calendário com datas de inscrição.

**Estudo e reforço:** conteúdo por matéria, ano/série e tópico; vídeos sugeridos, resumos, exercícios e provas para treinar; trilhas de reforço por dificuldade.

**Interação com professores:** espaço de dúvidas em que alunos perguntam e professores da rede respondem.

**Curadoria:** grupo de professores responsáveis por montar, revisar e atualizar o conteúdo de cada matéria, creditados como autores.

**Cuidados:** a rede atende principalmente crianças e adolescentes — moderação, login institucional e proteção de dados de menores (ECA e LGPD).

### 7.2 CI Eletrônica (comunicação interna formal)

Toda a comunicação formal da Secretaria sai do papel e tramita pelo portal: entre divisões, com as escolas e com órgãos externos. Hoje é em papel: demorado, burocrático, com risco de perda. Exige interfaces específicas e será um capítulo à parte.

**Estratégia:** a Prefeitura pretende adotar o SEI, mas isso deve demorar. A CI eletrônica ocupa esse intervalo com um sistema fácil de usar, que pode ser desativado depois (migrando o histórico) ou ampliado. Na proposta, aparece como solução de transição, não como concorrente do SEI.

**Funcionalidades previstas:**

- Numeração automática por setor e ano, no padrão atual (ex.: CI 157/VSV/2026), sem repetição.
- Modelo oficial pronto: o modelo de CI e a skill de documentos que William já tem viram o gerador dentro do sistema, com o mesmo timbre e layout.
- Tramitação com rastro: enviado, recebido, lido, despachado, respondido, arquivado — data, hora e responsável em cada passo.
- Assinatura eletrônica com validade jurídica (Lei 14.063/2020).
- Prazos e alertas para respostas pendentes, integráveis ao alerta em tempo real do sistema da recepção.
- Anexos, cópia para outros setores, busca por número, assunto, setor ou período.
- Arquivo permanente em PDF, respeitando prazos de guarda de documentos públicos.

### 7.3 Ouvidoria

O munícipe grava um áudio (transcrito automaticamente) ou escreve a mensagem para a Secretaria.

- Tipo: reclamação, sugestão, elogio, solicitação ou denúncia.
- Número de protocolo imediato para acompanhamento.
- Opção de identificação ou sigilo (Lei 13.460/2017 garante preservação da identidade).
- Prazo de resposta controlado (30 dias, prorrogáveis por mais 30, Lei 13.460/2017), com alerta ao setor responsável.
- Áudio original guardado junto da transcrição.
- Verificar se a Prefeitura tem Ouvidoria Geral: se tiver, encaminhar ou integrar, sem criar canal paralelo.

## 8. Banco de dados: encaixe no projeto Supabase "Portal Municipal"

O portal não cria banco novo: encaixa-se no projeto Supabase existente **Portal Municipal** (ref `qgywucdnaeheqndcxtho`, região sa-east-1, Postgres 17). Essa estrutura foi projetada para atender diversos órgãos públicos com o mesmo modelo e o mesmo projeto, com regras rigorosas de separação entre eles.

### 8.1 Tabelas existentes (schema public, todas com RLS ativo) e uso previsto

| Tabela(s) | Uso no Portal Educação |
| --- | --- |
| `municipios`, `municipio_dominios`, `orgaos` | Multiórgão: SMEDU como órgão dentro do município de Paulínia; domínio do portal |
| `equipe_plataforma` | Papel desenvolvedor/master (Secke) |
| `perfis`, `membros` | Ponto de partida de usuários e papéis |
| `destaques` | Carrossel de destaque (hero) |
| `publicacoes`, `publicacao_categorias`, `publicacao_midias`, `midias`, `categorias` | Notícias e mídias |
| `paginas`, `menus`, `menu_itens`, `redirecionamentos` | Páginas institucionais e navegação |
| `servicos` | Cards da Área de Serviços |
| `sistemas_externos` | Botões dos sistemas satélites |
| `eventos` | Agenda/eventos |
| `perguntas_frequentes` | FAQ |
| `documentos`, `documento_arquivos`, `documento_relacoes` | Documentos publicados |
| `transparencia_secoes`, `transparencia_itens`, `pntp_criterios`, `pntp_atendimento` | Transparência e critérios do PNTP |
| `auditoria` | Trilha de auditoria |
| `chamados`, `chamado_mensagens` | Suporte (avaliar uso para Ouvidoria) |
| `contratos`, `exportacoes`, `verificacoes_links`, `verificacao_problemas` | Gestão da plataforma |

### 8.2 Acréscimos previstos (sem quebrar o existente)

- Catálogo de permissões configurável por papel (seção 5.4) — não foram vistas tabelas de permissões; os papéis parecem fixos em `membros`.
- Papéis com escopo: tabela de unidades escolares (e regiões/setores) dentro do órgão, para vincular diretores.
- Vínculo escola → supervisor escolar (card 5).
- Equipe gestora: nível hierárquico, cargo, divisão, ordem, foto, visibilidade.
- Cards de aviso: prioridade, período de exibição, frequência por visitante — avaliar se `destaques` comporta ou se pede tabela própria.
- Grau de prioridade nas publicações (seção 4.2), se ainda não existir.

### 8.3 Regras

- Antes de qualquer migração: ler a estrutura completa (colunas, chaves, políticas RLS, funções) e entender o modelo de isolamento.
- Migrações aditivas; toda tabela nova com referência ao órgão/município e RLS desde o início, seguindo o padrão existente.
- Nenhum dado de um órgão visível a outro.

## 9. Requisitos transversais

- **Acessibilidade:** VLibras, alto contraste, aumento de fonte, navegação por teclado, textos alternativos, `prefers-reduced-motion` (Lei Brasileira de Inclusão, eMAG). Bem-feito, conta ponto na proposta.
- **LGPD:** aviso de cookies, política de privacidade, cuidado redobrado com dados de menores.
- **Responsivo e mobile first.**
- **Desempenho:** imagens otimizadas, carregamento rápido.
- **Auditoria:** ações administrativas registradas.
- **Gestão pelo painel:** carrossel, avisos, notícias, serviços, equipe, rodapé e botões de satélites editáveis pelo administrador, sem código.

## 10. Escopo da fase 1 e pendências

**Entra na fase 1 (piloto):**

- Portal público completo: cabeçalho, carrossel (3 slides), notícias, Área de Serviços (6 cards), seções temáticas, Equipe Gestora, rodapé, cards de aviso.
- Conteúdo real da carga inicial, com hierarquia de importância.
- Painel administrativo de conteúdo.
- Papéis e painel de permissões configuráveis (base para tudo que vier depois).
- Botões dos sistemas satélites, inativos/"em breve".

**Fica para fases futuras:** Área do Estudante, CI Eletrônica, Ouvidoria completa e integrações com Bolsa +, SIMAPE e apoio à recepção.

**Pendências a fornecer/confirmar:**

- [ ] Nomes e cargos da Equipe Gestora (William fornece)
- [ ] Autorização da Secretária e das pessoas para a seção Equipe Gestora
- [ ] Endereço, telefone e horário da SMEDU para o rodapé
- [ ] Códigos de cor do site oficial da Prefeitura e arquivo do brasão
- [ ] Vínculo escola → supervisor escolar
- [ ] Conteúdo das seções temáticas
- [ ] Existência de Ouvidoria Geral na Prefeitura
- [ ] Domínio/subdomínio definitivo
- [ ] Novos cards de serviço que William for lembrando
