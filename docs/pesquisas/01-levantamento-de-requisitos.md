# Pesquisas — Levantamento de Requisitos

> **Projeto:** Pesquisas (sistema satélite, autônomo) — Secke Tecnologias e Sistemas
> **Primeiro cliente:** Secretaria Municipal de Educação de Paulínia (SMEDU); cartão "Pesquisas da Educação" no Portal (D-126 do `portal-municipal`)
> **Situação:** brainstorming — sessão 1 em 25/10/2026 (rodadas 1 a 14) — **requisitos fechados para seguir ao banco**
> **Próxima etapa:** fechar as perguntas em aberto (seção 5) → funcionalidades consolidadas → telas/protótipo → banco → construção

Legenda: **D-xx** = decidido · **PR-xx** = proposta da Secke aguardando confirmação · **Q-xx** = pergunta em aberto

---

## 1. Contexto — como é hoje
- A Secretaria de Educação é complexa e precisa de interação intensa: entre departamentos, entre escolas, entre a Secretaria e as escolas, com os pais e com a comunidade. As demandas de pesquisa são muitas e variadas.
- **Não existe um sistema que centralize as pesquisas.** A prefeitura usa hoje um sistema que o William considera arcaico (Q-01), e o Google Forms aparece como referência de simplicidade, mas limitado.

## 2. Princípios
0. **O público é servidor público, culturalmente resistente a mudanças tecnológicas.** O sistema precisa ser **bonito e agradável** de usar, para quem cria e para quem responde, senão não é aceito (como na CI: mais fácil e mais gostoso que o jeito antigo).
1. **Sistema autônomo:** construído dentro do ecossistema do Portal, mas destacável: precisa funcionar em outros portais e sozinho, sem o portal. Critério fundamental.
2. **Multi-organização:** serve para qualquer secretaria ou prefeitura sem mudar código (D-10 do portal).
3. **Simples como o Google Forms para quem responde** (abre no celular, sem complicação) e **mais flexível que ele para quem cria**.
4. Padrões Secke: experiência do usuário no centro, linguagem humana, acessibilidade, painel com menu lateral, cabeçalho "onde estou".

## 3. O que já está DEFINIDO

### 3.1 Objetivo
- **D-01 — Centralizar as pesquisas da Secretaria**, em todas as suas dimensões e departamentos, para que os servidores, dentro das suas atribuições, criem e encaminhem pesquisas de um jeito simples.
- **D-02 — Resposta pelo celular de forma muito simples** (pais, familiares, servidores, comunidade), no nível do Google Forms.

### 3.2 Papéis (só três)
- **D-03 — Administrador:** mais de um por organização (flexibilidade e acompanhamento). Nomeia e remove gestores, promove gestor a administrador, cancela a conta de gestor.
- **D-04 — Gestor** (administrador setorial): tem conta com login; cria, encaminha e acompanha pesquisas.
- **D-05 — Destinatário:** quem responde. Papel passivo (pode haver campo de observações). **Por padrão todos são destinatários:** todo servidor da prefeitura, os pais e a comunidade.
- **D-06 — Toda mudança de papel fica registrada** (quem mudou, de quem, de quê para quê, quando).

### 3.3 Painel do gestor
- **D-07 — Painel com:** Minhas pesquisas · Pesquisas em andamento · Criar pesquisa · Pesquisas concluídas. Cada botão abre a tela do que precisa mostrar.

### 3.4 Criar pesquisa
- **D-08 — Escolha de layout primeiro:** "Criar pesquisa" abre um modal com desenhos simplificados de cada layout e o nome dele. A pessoa escolhe e segue.
- **D-09 — Formulário espaçoso:** título da pesquisa e **foto de destaque opcional** (enviada do computador). Sem foto, o sistema põe um fundo próprio com o título por cima.
- **D-10 — Perguntas:** campo para digitar a pergunta e, logo abaixo, **forma de resposta**:
  - **Escolha única:** lista de opções; fica claro para quem responde que só pode marcar uma;
  - **Várias escolhas:** pode marcar mais de uma;
  - **Gradiente (régua deslizante):** não é "de 1 a 5": é uma chavinha que a pessoa arrasta, mostrando a porcentagem, com o significado do começo e do fim escritos nas pontas (ex.: "Péssimo" … "Ótimo").
  - Novas formas de resposta podem entrar depois e valem em todo lugar.
- **D-11 — Subquestionário (tema e subtema):** em cada ponto a pessoa escolhe entre **criar uma pergunta** ou **criar um subquestionário**. O subquestionário tem título (o tema) e suas próprias perguntas, com as mesmas formas de resposta. Ex.: pesquisa ampla de necessidades, com subquestionários "Material", "Uniforme".

### 3.5 Assistente de IA ("o usuário nunca está sozinho")
- **D-12 — Assistente em segundo plano:** de tempos em tempos analisa o questionário que está sendo feito e sugere melhorias. Exemplos já citados: perguntas repetidas que deveriam virar subquestionário (sapato 41, sapato 36, uniforme 10…); pergunta ambígua, que pode ser mal interpretada ou mal redigida. O tom é educado e cortês. Novos pontos de análise serão acrescentados ao longo do brainstorm (lista na seção 6).
- **D-13 — Como a sugestão aparece:** um sinal alaranjado, chamando atenção, escrito "Sugestão". A pessoa escolhe **Abrir** ou **Ignorar**. Ao abrir: "Verifiquei que você fez isso… dá para fazer assim. Quer ver como fica ou seguir do seu jeito?".
- **D-14 — "Ver como ficaria":** o formulário muda na hora, e um modal pergunta **Adotar a mudança** ou **Voltar ao que era antes**. Voltar desfaz tudo e tira a sugestão.
- **D-15 — Assistente em primeiro plano:** sempre visível num canto da tela de criação ("Assistente de criação"). A pessoa fala em linguagem direta ("quero fazer essa parte assim e não sei como"); o assistente explica como fazer ou se oferece para fazer ele mesmo, e precisa ter condições de fazer.
- **D-16 — IA da Anthropic (Claude)**, pela chave de API da Secke.

### 3.6 Destinatários e grupos
- **D-17 — Cadastro de destinatários por classificação (segmentado):**
  - **Escolas** (a escola é o destinatário), divididas por **tipo** (creche, EMEI, EMEF, fundamental, PROEB… — lista oficial a ser fornecida pelo William, Q-13) e por **segmento de escolas** (outra divisão, Q-14);
  - **Departamentos** da Secretaria;
  - **Servidores da Educação**, divididos em **professor, administrativo, chefias** e "todos".
  - Em cada classificação: **selecionar todas** ou marcar uma a uma nas caixinhas.
- **D-18 — Busca de servidores:** campo de pesquisa com a lista de todos, mostrando **nome, cargo e lotação**; dá para escolher pessoas específicas e mandar direto para elas.
- **D-19 — Ferramenta "Criar grupo"** (não "selecionar destinatários"): ao montar o grupo a pessoa vê quem já está, adiciona, marca para excluir, e deixa o grupo pronto para usar de novo. Grupos podem misturar e fugir dos segmentos que já existem no sistema.
- **D-20 — Na hora de enviar a pesquisa:** **selecionar grupo**, **criar grupo** ou **selecionar destinatários** (pessoas específicas e os segmentos que o sistema já traz, incluindo todos os servidores da Educação).

- **D-21 — Segmentos e subsegmentos já sugeridos na criação do sistema** (a Secke monta a primeira árvore a partir do que conhece da rede); o administrador ajusta. Segmentos são **dados da organização**, não código (multi-organização). Ex.: Escolas → por tipo; Diretores de escolas → de todas ou das escolas X.
- **D-22 — Quem recebe pela escola:** a **secretaria da escola e o diretor**, sempre. (Detalhe de quem mais, a definir depois.)

### 3.7 Formulário de quem responde (design)
- **D-23 — Limpo e simples, pensado para um ser humano que precisa gostar do sistema**, senão não adere. Foto no alto, atraente.
- **D-24 — Opção "Outro":** quando nenhuma opção serve, a pessoa marca "Outro" e escreve.
- **D-25 — Campo de observação** para quem responde escrever o que quiser.
- **D-26 — Divisão bem clara entre uma pergunta e outra.**
- **D-27 — Subquestionário visível:** caixa própria, com cor diferente, e enunciados das perguntas na cor do tema, para deixar claro que pertencem ao mesmo tema.

### 3.8 Portal do destinatário e envio pelo WhatsApp
- **D-28 — Portal do destinatário:** o destinatário tem conta e uma área com **todas as pesquisas que respondeu**, para lembrar o que respondeu. Ao clicar, abre o formulário com as respostas enviadas, **fixas, sem poder corrigir**: servem como prova.
- **D-29 — Cadastro com celular/WhatsApp:** ao registrar diretores, coordenadores e demais destinatários, entra o número de celular com WhatsApp.
- **D-30 — Envio dos links pelo WhatsApp é o canal principal** (nada é mais rápido), pela API oficial da Meta, mesmo com custo por mensagem e o trâmite de aprovação.

### 3.9 Acompanhamento e resultados (gestor)
- **D-31 — Tela de entrada do gestor mostra, na área central, as pesquisas em andamento**, cada uma com: **% que já respondeu**, **data de início** e **meta de conclusão**.
- **D-32 — Barra de progresso clicável ("status"):** abre quantos responderam, quantos não responderam e **a lista de quem não respondeu**, para o gestor reforçar com essas pessoas.
- **D-33 — Padrão Secke de tela:** menu lateral esquerdo + cabeçalho.
- **D-34 — Menu "Resultados":** lista as pesquisas concluídas; ao abrir uma, o gestor **escolhe a forma de apresentar** os resultados.

- **D-35 — Meta de conclusão = data de encerramento.** Ao criar, o gestor informa **data de início** e **data de conclusão** (Q-23 respondida).
- **D-36 — Resultados parciais** podem ser vistos enquanto a pesquisa está em andamento, na própria tela de status (quem respondeu, quem não respondeu, quantos, e os resultados até agora) (Q-24 respondida).
- **D-37 — O resultado pertence a quem fez a pesquisa.** O **administrador não vê os resultados** das pesquisas: ele cuida de papéis, autorizações e novas ferramentas, não centraliza resultados (como já é hoje).

- **D-38 — Três meios de envio, sempre:** portal do destinatário, **e-mail** e **WhatsApp** (o cadastro guarda e-mail e WhatsApp).
- **D-39 — Uma resposta só, qualquer que seja o meio:** antes de abrir para responder, o sistema sabe se a pessoa já respondeu por outro meio.

- **D-40 — Cadeia de comando só por compartilhamento:** o chefe vê uma pesquisa só se o gestor compartilhar com ele (Q-26 respondida).
- **D-41 — Função "Compartilhar pesquisa":** botão já na criação da pesquisa. Compartilha-se **pelo nome da pessoa** (busca por nome, sem a segmentação, para não complicar). Quem recebe tem acesso aos **resultados parciais e ao resultado final**.

- **D-42 — Pesquisa aberta ao público (link/QR, sem cadastro):** padrão **uma resposta por aparelho**; para pesquisas em que a contagem precisa ser exata, o gestor liga **código no celular** (uma resposta por número). Ex.: pesquisa de satisfação aberta na escola ("como você foi atendido"). (Q-27 respondida; PR-36 adotada sem a opção "livre".)

- **D-43 — Banco no projeto Supabase "Portal Municipal"** (sem projeto separado enquanto não há arrecadação), no schema próprio `pesquisa`, construído para poder ser **isolado e recriado num projeto à parte** ou usado em outros portais (confirma a PR-01).

### 3.10 Respostas da rodada de 25/10 (fechamento antes do banco)
- **D-44 — Sem coautoria:** só o dono edita a pesquisa; o compartilhamento é só para ver resultados (Q-02).
- **D-45 — Aprovação antes de sair para pais e comunidade:** pesquisa de uma escola → aprovação da **diretora da escola**; pesquisa mais ampla → aprovação da **Secretária** (Q-03). Detalhada na D-54.
- **D-46 — Anônima ou identificada: o gestor escolhe** em cada pesquisa (Q-05).
- **D-47 — Para responder: uma pergunta por tela** (o celular é o principal). Seta para avançar e seta para voltar; a pessoa revê todas as respostas e, no fim, **salva as respostas**. A tela de montar continua mostrando o questionário inteiro (Q-07).
- **D-48 — Subquestionário só em um nível.** Nunca subquestionário dentro de subquestionário (Q-08).
- **D-49 — Dependência entre perguntas:** se a pessoa responde "Sim" a uma, é levada à pergunta que depende desse "Sim" (Q-10; forma proposta na PR-40).
- **D-50 — Pesquisa para escolas: uma resposta por escola**, seja do diretor ou do secretário de escola (Q-15).
- **D-51 — Grupos compartilháveis:** quem cria o grupo pode compartilhá-lo com outros gestores. Todo grupo tem uma **descrição básica** ("este grupo contém…"), escrita pela pessoa ou gerada pelo sistema (Q-16).
- **D-52 — Chefias são cadastradas:** a pessoa é marcada como chefia, com a divisão que chefia (Q-18).
- **D-54 — Só pesquisas para pais e comunidade precisam de aprovação** (para servidores e escolas, não). Pesquisa de uma unidade → aprova o **gestor da unidade** (diretor escolar ou outra pessoa classificada como gestora da unidade). Pesquisa ampla, da Secretaria ou da educação como um todo → aprova o(a) **Secretário(a) de Educação** (Q-31).
- **D-55 — Propostas PR-01 a PR-43 aprovadas em bloco** em 25/10/2026, exceto as já substituídas (PR-29 pela D-41; PR-36 ajustada pela D-42). Daqui em diante valem como decisões.
- **D-53 — Pais e comunidade não têm conta:** entram pelo link/QR e respondem; o portal do destinatário é só para quem está cadastrado (Q-22).

## 4. Propostas da Secke (aguardando confirmação)
- **PR-01 — Arquitetura autônoma:** repositório e aplicativo próprios; schema `pesquisa` no mesmo Supabase; ligação com o portal só por uma camada fina (organização, login, cartão na página inicial). Sem o portal, a mesma camada usa cadastro próprio de organização e usuários.
- **PR-02 — Ciclo da pesquisa:** Rascunho → (revisão, se a organização exigir) → Agendada → Aberta → Encerrada (na data ou à mão) → Concluída (resultados) → Arquivada.
- **PR-03 — Destinatário responde sem login** (link ou QR Code), salvo quando a pesquisa exigir identificação.
- **PR-04 — O "setor" do gestor vem da estrutura da organização** (departamentos, divisões, escolas), a mesma estrutura usada pela CI, para limitar o que cada gestor vê e para escolher o público.

- **PR-05 — Layouts iniciais:** (a) Clássico: capa com foto e perguntas em lista; (b) Uma por vez: uma pergunta por tela, ideal no celular; (c) Cartões: cada tema num cartão; (d) Oficial: com o timbre da organização, para levantamentos internos.
- **PR-06 — Mais formas de resposta:** texto curto, texto longo, número, sim/não, data, **quantidades** (lista de itens com um número para cada, ex.: tamanhos de sapato), tabela (mesma escala para vários itens), anexo de foto/arquivo.
- **PR-07 — Subquestionário repetível:** "responder para cada filho" ou "para cada turma", repetindo o mesmo bloco.
- **PR-08 — Toda mudança feita pela IA (sugestão ou chat) passa por "Ver como ficaria" → Adotar/Voltar**, e há sempre "Desfazer". A IA nunca altera sozinha.
- **PR-09 — Sugestão ignorada não volta** (a mesma sugestão para o mesmo trecho).
- **PR-10 — Chave da IA só no servidor** (Edge Function do módulo), nunca no navegador; IA ligável por organização, com limite de uso; para a IA vai só o texto do questionário, nunca as respostas das pessoas (resumo de respostas, se houver, é decisão à parte).
- **PR-11 — O sinal de sugestão pulsa suavemente** (sem piscar forte, respeitando quem pede menos movimento) e pode ser ouvido, como as mensagens da CI.
- **PR-12 — Grupo vivo:** um grupo pode guardar um segmento inteiro ("todas as EMEIs"), que se atualiza sozinho quando entra uma escola nova, ou uma lista fixa de nomes; e pode ter exceções ("todas as EMEIs, menos a X"). O grupo mostra sempre o total (ex.: "59 escolas · 312 pessoas").
- **PR-13 — Cadastro aproveitado, sem depender:** escolas e departamentos vêm da estrutura já cadastrada no portal e na CI; servidores, da lista de pessoas da CI (nome, cargo, lotação), por importação ou sincronização. Sozinho, o sistema tem cadastro e importação por planilha próprios (autonomia, PR-01).
- **PR-14 — Link pessoal para pesquisa dirigida:** cada destinatário recebe um link próprio (sem login), para o sistema saber quem já respondeu e cobrar quem falta, sem que a pessoa precise de conta.
- **PR-15 — Envio:** e-mail (depende do servidor de e-mail da Prefeitura, a mesma pendência da CI), botão "Enviar pelo WhatsApp" que abre a conversa com a mensagem e o link prontos, aviso na caixa da CI (quando a organização usa a CI) e QR Code para cartaz ou bilhete.
- **PR-16 — Árvore inicial de segmentos (SMEDU, 59 unidades do cadastro do portal em 25/10/2026):**
  - **Escolas por tipo:** Creches (18) · EMEIs (14) · EMs (12) · EMEFs (9) · EMEFMs (2) · EMEFI (1) · Supletivo/EJA (1) · Escolas técnicas (2, CEMEP e ETEP) · Conveniadas PROEB (ainda não cadastradas no portal).
  - **Escolas por etapa:** Educação Infantil (Creche, Pré-escola) · Fundamental I · Fundamental II · Ensino Médio · EJA · Técnico. Uma escola pode estar em mais de uma etapa.
  - **Escolas por região** (o cadastro do portal já tem região).
  - **Pessoas da escola:** Diretores · Vice-diretores · Coordenadores pedagógicos · Professores · Secretaria escolar e apoio.
  - **Departamentos da Secretaria** (organograma já cadastrado).
  - **Servidores da Educação:** Professores · Administrativos · Chefias · Todos.
- **PR-17 — "Quem" × "Onde":** um segmento de pessoas cruza com um segmento de escolas: "Diretores" + "EMEIs" = "Diretores das EMEIs"; "Professores" + "Fundamental II" + "Região Norte". O total aparece na hora.
- **PR-18 — Cor do tema com reforço:** cada subquestionário recebe uma cor de uma paleta com bom contraste, e também o nome do tema no alto da caixa (quem não distingue cores entende do mesmo jeito).
- **PR-19 — Conforto de quem responde:** barra de progresso ("3 de 8"), tempo estimado na capa, botões grandes para o dedo, "Continuar depois" sem perder o que já respondeu, aviso gentil do que faltou, tela final de agradecimento, identidade da organização (brasão e cores) e leitura em voz alta.
- **PR-20 — Entrar sem senha:** o destinatário entra no seu portal com um código enviado pelo WhatsApp (ou pelo login do portal/CI, se for servidor). O link da pesquisa já identifica a pessoa.
- **PR-21 — Comprovante:** ao enviar, a pessoa recebe um comprovante com número, data e hora e um QR Code de verificação (como a CI). Respostas gravadas não mudam; qualquer alteração seria detectada.
- **PR-22 — Pesquisa anônima no portal do destinatário:** aparece só como "Respondida em 12/11", sem as respostas, porque guardar o vínculo pessoa ↔ resposta quebraria o anonimato. A cópia das respostas fica só com a pessoa (PDF baixado na hora). Q-21.
- **PR-23 — WhatsApp da própria organização:** cada organização usa um número verificado em seu nome ("Secretaria de Educação de Paulínia"), o que dá confiança e evita golpe; a Secke configura. Mensagens por modelos aprovados pela Meta (convite, lembrete, encerramento), com "Parar de receber" e consentimento registrado (LGPD). Sem conta configurada, o envio cai no botão "Enviar pelo WhatsApp" manual.
- **PR-24 — Lembretes automáticos** para quem não respondeu (ex.: 2 dias antes do fim), com limite para não incomodar.
- **PR-25 — Cobrar direto do status:** na lista de quem não respondeu, botões "Lembrar todos" e "Lembrar" um a um (WhatsApp), mostrando quando foi o último lembrete. Pesquisa dirigida a escolas mostra a escola e o diretor responsável.
- **PR-26 — Participação separada do conteúdo:** o sistema sabe *quem respondeu* (para cobrar) sem ligar a pessoa às respostas quando a pesquisa é anônima.
- **PR-27 — Formas de apresentar os resultados:**
  1. **Painel visual** (padrão): um cartão por pergunta, com gráfico de barras e percentuais; gradiente com média ("satisfação média 72%") e distribuição; **quantidades somadas** (ex.: sapato 41: 120 pares; uniforme 10 feminino: 85), com total por escola;
  2. **Comparar** por escola, tipo, etapa ou região (filtros e gráfico lado a lado);
  3. **Relatório em PDF** no molde Secke (capa com a foto da pesquisa, resumo, gráficos, respostas abertas), pronto para imprimir;
  4. **Apresentação** em tela cheia, um slide por pergunta, para reunião;
  5. **Planilha** (Excel/CSV) com todas as respostas, para quem quer trabalhar os dados;
  6. **Respostas abertas e "Outro"** em lista, com busca; agrupamento por assunto feito pela IA (depende do de acordo de uso de IA, Q-12).
- **PR-28 — Proteção do anonimato nos filtros:** em pesquisa anônima, um recorte com menos de 5 respostas (ex.: uma escola pequena) não é mostrado separado.
- **PR-29 — (substituída pela D-41).**
- **PR-30 — Pesquisa não fica órfã:** se o gestor sai ou perde o papel, o administrador **transfere** as pesquisas dele para outro gestor, sem abrir os resultados; fica registrado.
- **PR-31 — Administrador vê só o "envelope":** título, quem criou, situação, datas e número de respostas (para acompanhar o uso do sistema), nunca as respostas.
- **PR-32 — Um convite por pessoa, válido nos três meios:** cada destinatário tem um único convite por pesquisa; o link do e-mail, o do WhatsApp e o botão do portal apontam para ele. O servidor confere na abertura e de novo na hora de enviar (trava no banco: duas respostas ao mesmo convite são impossíveis, mesmo em dois aparelhos ao mesmo tempo).
- **PR-33 — Se já respondeu:** abre "Você já respondeu em 12/11 às 10h15, pelo WhatsApp", com o botão do comprovante (ou das respostas, se identificada). Sem mensagem de erro.
- **PR-34 — Rascunho acompanha a pessoa:** começou no celular e parou, continua no computador de onde parou, por qualquer dos três meios.
- **PR-35 — Respondeu, param os lembretes** nos três meios.
- **PR-36 (adotada na D-42) — Pesquisa aberta (link público, sem cadastro):** não há como garantir uma por pessoa sem identificar; opções por pesquisa: livre, uma por aparelho, ou confirmar o celular com um código (uma por número). Q-27.
- **PR-37 — Detalhes do compartilhamento:** a busca mostra nome, cargo e lotação (como na D-18); dá para compartilhar também depois de criada; quem recebe é avisado (WhatsApp/e-mail) e encontra a pesquisa em "Compartilhadas comigo"; o dono pode **retirar** o acesso a qualquer momento; tudo fica registrado.
- **PR-38 — Quem recebe o compartilhamento só vê** (resultados, PDF e planilha), não edita a pesquisa nem compartilha de novo. Se não for gestor, entra pelo portal do destinatário/login do portal e vê só as pesquisas compartilhadas com ele.
- **PR-39 — Pesquisa permanente:** uma pesquisa sem data de fim (ex.: satisfação do atendimento na secretaria da escola), com QR Code em cartaz no balcão e resultados por mês, para acompanhar a evolução. Q-29.
- **PR-40 — Como montar a dependência (D-49):** em cada pergunta ou subquestionário, o gestor liga "Mostrar só se…" e completa uma frase com listas: *Mostrar esta pergunta só se* [pergunta 3] *for* [Sim]. Pode juntar condições ("e"/"ou"). A pergunta dependente ganha uma etiqueta "Depende da 3" na tela de montar. Para quem responde, nada aparece: a pergunta só surge quando vale. Se a pessoa volta e muda a resposta, a pergunta dependente some e o que foi respondido nela é descartado. O sistema não deixa depender de uma pergunta que vem depois (evita laço), e o assistente de IA ajuda a montar ("quero que só quem tem filho na creche responda isto").
- **PR-41 — Fluxo de aprovação (D-45):** público de uma única escola → a diretora dessa escola aprova; mais de uma escola ou público geral → a Secretária aprova (quem aprova cada caso fica na configuração da organização). Quem aprova recebe o pedido por WhatsApp/e-mail, vê a pesquisa como o público verá e escolhe **Aprovar** ou **Devolver com comentário**. Só depois de aprovada a pesquisa abre. Tudo registrado.
- **PR-42 — Descrição automática do grupo (D-51):** o sistema escreve sozinho a partir do que foi escolhido, sem IA ("Todas as EMEIs, menos a EMEI X · 13 escolas · diretores e secretários"); a pessoa pode editar.
- **PR-43 — Pais sem conta (D-53):** no fim da pesquisa, botão "Baixar minhas respostas" (PDF) como comprovante.

## 5. Perguntas em aberto (revisadas em 25/10/2026)

Respondidas e já levadas para a seção 3: Q-04 (D-38), Q-06 (D-37), Q-23 (D-35), Q-24 (D-36), Q-26 (D-40), Q-27 (D-42).

### 5.1 Precisam de resposta antes do banco
Respondidas em 25/10: Q-02, Q-03, Q-05, Q-07, Q-08, Q-10, Q-15, Q-16, Q-18, Q-22 (seção 3.10).
Respondidas também: Q-30 (D-55) e Q-31 (D-54). **Nada mais trava o banco.**

### 5.2 Podem ficar para depois (não travam o banco)
- **Q-01** Sistema usado hoje e o que falta no Google Forms (ajuda no discurso da apresentação).
- **Q-09** Gradiente: mostrar o número enquanto arrasta?
- **Q-11 / Q-20** Pergunta obrigatória, "Outro" e observação: padrões (proposta: gestor liga por pergunta; uma observação no fim por padrão).
- **Q-12** De acordo da SMEDU para usar IA (pendência da CI; sem ele o assistente fica desligado).
- **Q-13 / Q-14 / Q-19** Lista oficial de tipos e segmentos de escola e etapa das EMs/EMEFs (dados, entram pelo cadastro).
- **Q-21** Pesquisa anônima no portal do destinatário mostra só "respondida".
- **Q-25** Resultado pode ser publicado no portal?
- **Q-28** Quem recebe compartilhamento pode baixar PDF/planilha?
- **Q-29** Pesquisa permanente.

## 6. Pontos que a IA analisa (lista viva)
1. Perguntas parecidas em sequência que deveriam virar subquestionário (ou o tipo "quantidades").
2. Pergunta ambígua, mal redigida ou que pode ser mal interpretada.
3. (propostas) Duas perguntas em uma ("O lanche é gostoso e suficiente?"); pergunta que induz a resposta; opções que não cobrem todos os casos ou se sobrepõem (faixas de idade); forma de resposta que não combina com a pergunta; linguagem difícil para as famílias; dado pessoal desnecessário ou sensível (LGPD); pesquisa longa demais (tempo estimado).
