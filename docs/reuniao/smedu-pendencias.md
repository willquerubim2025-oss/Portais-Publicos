# Pendências com a SMEDU (Secretaria Municipal de Educação de Paulínia)

**Tudo o que depende da Secretaria ou da Prefeitura fica neste documento.** É a lista para levar às reuniões e para cobrar o material.

**Como trabalhamos enquanto a resposta não chega (combinado com o William em 15/10/2026):**
- não paramos: usamos **dado público** (site da Prefeitura, imprensa), **foto de banco de imagens** com licença livre ou um **placeholder**, e seguimos;
- cada coisa provisória fica marcada aqui, com o que está no site hoje, para trocar quando chegar o material;
- só paramos e cobramos a Secretaria se a falta **travar** o trabalho;
- quando um item for resolvido, marcar como ~~riscado~~ com a data e o que mudou.

Cada item traz: o que precisamos · o que está no site hoje · onde será usado · se bloqueia ir ao ar.

## Resumo

| # | Assunto | No site hoje | Bloqueia ir ao ar? |
|---|---|---|---|
| 1 | E-mail oficial da Secretaria | `educacao@paulinia.sp.gov.br` | Não |
| 2 | Supervisores de cada escola | "Supervisor ainda não informado" | Sim (função principal do "Fale com o Supervisor") |
| 3 | Erros na lista de escolas | dados da fonte pública | Não |
| 4 | Etapas de cada escola | só creches, EMEIs e algumas | Não |
| 5 | Matrícula 2027 | **provisória**: datas de 2027 de notícias (15/10) | Sim, antes do período de matrícula |
| 6 | Números da rede | números da imprensa e do Censo | Não |
| 7 | Equipe gestora e organograma | 10 pessoas **fictícias** com fotos de banco | Sim (dados fictícios) |
| 8 | Páginas legais: Acesso à Informação, Ouvidoria, Privacidade | **provisórias** com dados públicos (15/10) | Sim (confirmar antes de ir ao ar) |
| 9 | Autorização de imagem das fotos | fotos novas do "Em foco" e notícias com crianças | Sim (ECA/LGPD) |
| 10 | Brasão em alta resolução | brasão de 252 px | Não |
| 11 | Dados institucionais e acesso | sem domínio, IBGE, CNPJ e administrador | Sim |
| 12 | Menu principal | 6 itens definidos pela Secke | Não |
| 13 | Bolsa de Estudo | **provisória** com dados públicos (15/10) | Não |
| 14 | Agenda de eventos | 6 eventos **fictícios** + 1 real | Sim (dados fictícios) |
| 15 | Área do Estudante e Ouvidoria | **provisórias**: montadas com o que o portal já tem (15/10) | Não |
| 16 | Notícias | 7 notícias do site da Prefeitura, datas aproximadas | Não |
| 17 | Transparência: contas públicas e conselhos | atalho para o site da Prefeitura; conselhos sem documentos | Não |
| 18 | Sistemas usados pelos servidores | nenhum cadastrado para a SMEDU | Não (sim para a "central de ferramentas") |

Fonte da carga inicial (12/10/2026, homologação): a página da Secretaria de Educação em www.paulinia.sp.gov.br, atualizada em 04/09/2026. Cada unidade tem `legado.confirmar = true` no banco.

## 1. E-mail oficial da Secretaria
- **O que precisamos:** saber qual e-mail vai no rodapé. A página oficial mostra dois: `educacao@paulinia.sp.gov.br` e `se@paulinia.sp.gov.br`. Por enquanto o rodapé usa `educacao@`.
- **Onde será usado:** rodapé de todas as páginas.
- **O que muda:** só o texto (config.email).
- **Bloqueia?** Não.

## 2. Supervisores de ensino por escola
- **O que precisamos:** para cada uma das 59 unidades, o supervisor responsável (nome, e-mail e telefone institucionais) e a autorização para publicar esses dados.
- **Onde será usado:** busca "Escolas e supervisores" (/fale-com-o-supervisor). Hoje cada escola mostra "Supervisor ainda não informado".
- **O que muda:** com os dados, a busca passa a mostrar o contato do supervisor.
- **Bloqueia?** Bloqueia a função principal do card "Fale com o Supervisor".

## 3. Erros na lista oficial de escolas
- **O que precisamos:** que a SMEDU confirme ou corrija:
  - **E.M. Atílio Bardin:** o e-mail na fonte é `em-elaine@`;
  - **E.M. Rosa Vassalo Secomandi:** o e-mail na fonte é `emei-rosa@`;
  - **EMEF Prefeito José Lozano:** o e-mail na fonte é `emefm-lozano@`;
  - **ETEP:** está sem CEP;
  - **EMEFI Simone Martinez:** a lista oficial põe a escola no Jardim Planalto e uma notícia, no Patropi.
- **Onde será usado:** busca de escolas.
- **O que muda:** só os dados de cada unidade.
- **Bloqueia?** Não.

## 4. Etapas atendidas por escola
- **O que precisamos:** as etapas que cada EM, EMEF e EMEFI atende (pré-escola, anos iniciais, anos finais, integral).
- **Onde será usado:** filtros e informação da busca de escolas.
- **O que muda:** o campo `etapas`. Hoje só está preenchido para creches, EMEIs, EMEFMs, supletivo e técnicas.
- **Bloqueia?** Não.

## 5. Matrícula 2027
- **O que precisamos:**
  - o cronograma de 2027 (Fundamental e EJA);
  - os documentos exigidos no Fundamental;
  - a faixa etária de cada ano.
- **No site hoje (provisório, desde 15/10/2026):** a página Matrícula Escolar ganhou o bloco "Vagas para 2027", com datas de notícias locais: **Ensino Fundamental até 23/10/2026** (só para quem ainda não é da rede) e **creches e EMEIs até 11/12/2026**, pelo site `paulinia.sp.gov.br/matriculaescolar`. **Confirmar:** uma das notícias dá 12/11 no título para creches e EMEIs; e há uma notícia da Prefeitura sobre "suspensão temporária de inscrições e transferências para a Educação Infantil" (ver se ainda vale). O resto da página (documentos, SISS, EJA) é do ciclo de 2026.
- **Onde será usado:** página Matrícula Escolar e o card da página inicial.
- **O que muda:** o texto da página e, talvez, um aviso ou slide na home durante o período.
- **Bloqueia?** Não para a homologação; sim antes do período de matrícula.

## 6. Números da rede
- **O que precisamos:** que a Secretaria valide os números.
  - O IDEB 2025 (6,7 nos anos iniciais e 5,0 nos finais) veio da imprensa local, não do INEP.
  - As fontes divergem no total de alunos: cerca de 11 mil (Prefeitura, fev/2026), 13.934 (Censo 2025, ensino regular) e 16.353 (imprensa, contando EJA e educação especial).
- **Onde será usado:** página Educação em Números.
- **O que muda:** os números e a fonte citada.
- **Bloqueia?** Não.

## 7. Equipe gestora e organograma
- **O que precisamos:**
  - nomes e cargos da equipe gestora (Secretária, Adjunto(a), supervisores e diretores de divisão);
  - autorização para publicar;
  - fotos, se autorizadas;
  - organograma com as divisões.
- **O que já sabemos:** a fonte pública cita a Secretária Márcia Scarassati.
- **No site hoje:** 10 pessoas **fictícias** (Secretária, Adjunto, 3 supervisores e 5 diretores), com fotos de banco de imagens, para a apresentação. No banco, o resumo começa com "FICTÍCIO".
- **Onde será usado:** seção Equipe gestora na home e na página Estrutura organizacional. O card "Secretaria de Educação" leva à Estrutura organizacional.
- **O que muda:** trocamos as pessoas fictícias pelas reais. Sem foto autorizada, o site mostra as iniciais (nunca foto de banco para pessoa real).
- **Bloqueia ir ao ar?** Sim: os nomes fictícios precisam sair.

## 8. Páginas obrigatórias do rodapé: Acesso à Informação, Ouvidoria e Privacidade
- **O que precisamos:**
  - **Acesso à Informação e e-SIC (Lei 12.527/2011):** o link do pedido eletrônico de informação da Prefeitura (o e-SIC atende a Secretaria ou ela tem canal próprio?), endereço e horário do atendimento presencial, prazos e como recorrer;
  - **Ouvidoria (Lei 13.460/2017):** o canal da Ouvidoria que atende a Educação (link, e-mail, telefone e endereço) e se a Secretaria tem ouvidor próprio;
  - **Privacidade (LGPD, Lei 13.709/2018):** nome e e-mail do encarregado de dados (DPO) da Prefeitura e, se existir, a política de privacidade oficial para seguirmos o mesmo texto.
- **Onde será usado:** links do rodapé de todas as páginas (Acesso à Informação, Ouvidoria, Privacidade) e o card "Ouvidoria" dos Serviços.
- **No site hoje (provisório, desde 15/10/2026):** as três páginas foram escritas e publicadas na homologação com **dados públicos**, e estão marcadas no banco com `legado.provisorio = true`:
  - Ouvidoria e Acesso à Informação apontam para a Ouvidoria da Prefeitura: telefone 156 ou (19) 3874-5600, `ouvidoria@paulinia.sp.gov.br` (achado em página da Câmara de Paulínia, que replica os contatos da Prefeitura; o site da Prefeitura esconde o e-mail), Paço Municipal, de segunda a sexta, das 8h às 17h, e o link `https://www.paulinia.sp.gov.br/portal/ouvidoria`. **Não achamos e-SIC próprio da Prefeitura** (a Câmara usa o Fala.BR);
  - Privacidade descreve o que o portal coleta (sem cadastro, sem cookies de rastreamento, só preferências de acessibilidade no navegador) e manda os pedidos da LGPD para a Ouvidoria, **sem nome de encarregado**;
  - **confirmar:** o canal de pedido de informação (e-SIC ou Fala.BR?), o e-mail da Ouvidoria e o encarregado de dados. Fontes: [Ouvidoria da Câmara de Paulínia](https://www.camarapaulinia.sp.gov.br/ouvidoria/) e [Ouvidoria da Prefeitura](https://www.paulinia.sp.gov.br/portal/ouvidoria). A página de **Acessibilidade** já foi escrita e publicada na homologação em 15/10/2026, com o e-mail e o telefone da Secretaria (confirmar se são esses os canais para relatar problemas).
- **Bloqueia?** Não para a homologação; **sim antes de ir ao ar** (são exigências legais e entram na avaliação do PNTP).

## 9. Autorização de imagem das fotos
- **O que precisamos:**
  - **"Em foco", Matrícula:** autorização de imagem da foto da criança chegando à escola com a família (pessoas reconhecíveis, ECA e LGPD) e a origem da foto;
  - **"Em foco", Bolsa de Estudo:** a origem e a licença da foto dos estudantes na escadaria (parece de banco de imagens ou gerada);
  - **notícias:** as 7 notícias vieram do site da Prefeitura e algumas têm fotos com crianças. Confirmar que podemos republicá-las.
- **No site hoje:** as fotos novas já estão no "Em foco" da homologação desde 15/10/2026.
- **Bloqueia ir ao ar?** Sim. Sem autorização, trocamos por foto de banco com licença livre ou sem pessoas reconhecíveis.

## 10. Brasão oficial em alta resolução
- **O que precisamos:** o brasão da Prefeitura em PNG com fundo transparente (pelo menos 1000 px) ou em SVG.
- **No site hoje:** o brasão recebido tem só 252 px. Serve no cabeçalho e no rodapé, mas fica ruim no compartilhamento em redes sociais e na impressão.
- **Bloqueia ir ao ar?** Não.

## 11. Dados institucionais e acesso ao painel
- **O que precisamos:**
  - o **domínio** do portal (ex.: `educacao.paulinia.sp.gov.br`) e quem cuida do DNS na Prefeitura, para apontarmos o endereço;
  - **código IBGE** e **CNPJ** usados na Central de Transparência e nos dados estruturados;
  - quem será o **primeiro Administrador** do painel na Secretaria (nome e e-mail institucional). Só a Secke faz esse primeiro vínculo; depois a própria Secretaria convida os demais.
- **No site hoje:** a homologação usa o endereço provisório `portal-municipal-homologacao.willquerubim2025.workers.dev`; IBGE e CNPJ vazios; no painel, só usuários de teste da Secke.
- **Bloqueia ir ao ar?** Sim.

## 12. Menu principal
- **O que precisamos:** que a Secretaria aprove os rótulos e a ordem do menu.
- **No site hoje:** Início · A Secretaria (Equipe gestora, Estrutura organizacional, Legislação, Documentos, Perguntas frequentes) · Matrícula · Escolas e supervisores · Notícias · Serviços. Agenda e Transparência saíram do menu do cabeçalho em 15/10/2026 (D-64), para caber numa linha; as páginas continuam no site.
- **Bloqueia ir ao ar?** Não.

## 13. Bolsa de Estudo
- **O que precisamos:** as regras do programa municipal de bolsas: quem pode se inscrever, prazos, documentos, como sai o resultado e como renovar.
- **No site hoje (provisório, desde 15/10/2026):** a página `/servicos/bolsa-de-estudo` foi preenchida com dados públicos do **Programa Bolsa Educação** (notícias da Prefeitura e imprensa local; `legado.provisorio = true`): 10 anos de residência, renda de até 10 salários mínimos, bolsa de 100% (até 6 salários) ou 50% (6,1 a 10), cadastro no PAS de 19/10 a 11/12/2026 para o ciclo 2027 pelo telefone (19) 3874-5741, 20 horas mensais de contrapartida, 420 contemplados em 2026 e link para `paulinia.sp.gov.br/bolsaeducacao`.
- **Confirmar:** se o programa é da Secretaria de Educação (a página fica no portal dela), o limite de renda e as datas de 2027, a lista de instituições conveniadas e se a nota do Enem 2026 conta na seleção.
- **Bloqueia ir ao ar?** Não, mas é um dos dois destaques do "Em foco".

## 14. Agenda de eventos
- **O que precisamos:** o calendário real da Secretaria (eventos, formações, reuniões de pais, datas do calendário escolar) e quem vai mantê-lo.
- **No site hoje:** 6 eventos **fictícios** e 4 órgãos fictícios, para a apresentação. Só a prova do Vestibulinho (18/10) é real.
- **Bloqueia ir ao ar?** Sim: os eventos fictícios precisam sair.

## 15. Área do Estudante e Ouvidoria (eram "Em breve")
- **O que precisamos:** decidir com a Secretaria o que entra em **Área do Estudante** (estudo, reforço, vestibulinhos, contato com professores) e como funciona a **Ouvidoria** da Educação (ligada ao item 8).
- **No site hoje (provisório, desde 15/10/2026):** os dois cards saíram do "Em breve". A **Área do Estudante** reúne o que o portal já tem: Vestibulinho do CEMEP e da ETEP (prova em 18/10), Bolsa Educação, uniforme 2027, matrícula, busca de escolas e agenda. A descrição antiga falava em "reforço e contato com professores", que não existem: saiu. O card **Ouvidoria** leva à página /ouvidoria (a descrição antiga dizia "por áudio ou texto", que não existe).
- **Confirmar:** se a Secretaria quer reforço escolar, materiais de estudo ou contato com professores na Área do Estudante, e se haverá ouvidoria própria da Educação (com áudio, como a especificação sugeria).
- **Bloqueia ir ao ar?** Não. Podem sair da página até ficarem prontos.

## 16. Notícias
- **O que precisamos:** quem da Secretaria vai publicar as notícias e se as 7 notícias trazidas do site da Prefeitura ficam no portal.
- **No site hoje:** 7 notícias reais do site da Prefeitura, com crédito e link. As datas são aproximadas (o site da Prefeitura não mostra a data de cada notícia), exceto a do uniforme (09/10).
- **Bloqueia ir ao ar?** Não.

## 17. Transparência: contas públicas e conselhos
- **O que precisamos:**
  - o **endereço do Portal da Transparência da Prefeitura** (receitas, despesas, licitações, contratos, servidores), para o atalho "Contas Públicas" levar direto a ele;
  - se a Secretaria publica **licitações, contratos ou convênios próprios** (ex.: alimentação escolar, transporte), ou se tudo fica no portal da Prefeitura;
  - os **conselhos** ligados à Educação (Conselho Municipal de Educação, CACS-FUNDEB, Conselho de Alimentação Escolar): composição, atas e contatos;
  - o **Plano Municipal de Educação** (lei e relatórios de monitoramento) e outros planos e programas que devem aparecer.
- **No site hoje:** desde 15/10/2026 (D-90), a Transparência da SMEDU tem o pacote de **secretaria**: Informações Institucionais, Contas Públicas (atalho para `www.paulinia.sp.gov.br`, porque não achamos o endereço do portal de transparência), Editais/Convênios/Seleções, Conselhos, Planos e Relatórios, Acesso à Informação, Ouvidoria, Privacidade e Acessibilidade. As categorias de documentos estão vazias.
- **Bloqueia ir ao ar?** Não, mas a Transparência entra na avaliação do PNTP.

## 18. Sistemas usados pelos servidores
- **O que precisamos:**
  - a lista dos sistemas que os servidores da Educação usam hoje (ex.: matrícula/SISS, sistema de gestão escolar, diário de classe, folha/RH, protocolo, SEI, Bolsa +, SIMAPE), com o endereço de cada um;
  - quem usa cada sistema (Secretaria, diretores, secretários de escola, professores);
  - como é o login em cada um (conta própria, conta da Prefeitura, gov.br);
  - se todos os servidores têm **e-mail institucional** (é o que usaremos para o login do painel e dos satélites).
- **Onde será usado:** a "central de ferramentas" do servidor no painel (atalhos por papel) e o plano de login único com os sistemas satélites (`docs/Roteiro para Concluir.md`, seção 1).
- **Bloqueia ir ao ar?** Não. Sem a lista, o painel abre só com as ferramentas de conteúdo.
