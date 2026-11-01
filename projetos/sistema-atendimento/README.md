# Sistema de Atendimento para Restaurantes e Lanchonetes

Projeto separado dos Portais Públicos. Fica guardado aqui até ganhar um repositório próprio. Quando o repositório existir, mover esta pasta para lá.

Origem: conversa de 31/10 e 01/11/2026 com o William, a partir do documento "Projeto de Sistema de Pedidos Inteligente por Mesa — Versão 1.0".

---

## 1. O que vamos vender

**O foco é o atendimento:** atendimento mais rápido, com menos erro e mais fácil de rastrear e controlar.

Junto com o atendimento vão **ferramentas básicas de gestão**. Muitas lanchonetes vendem bem, mas não têm nenhum sistema de gestão. O produto fica **aberto para virar um sistema completo**, mas sem perder o foco no atendimento.

---

## 2. Decisões tomadas

### A-01: terminal próprio com ESP32 fica para depois
- O terminal ESP32-S3 com tela de 5" é viável tecnicamente, mas custa de **R$ 350 a 535** no protótipo. A meta original era R$ 250. Também exige homologação na ANATEL (R$ 15 a 40 mil), molde da caixa e firmware próprio.
- Com um tablet básico custando de R$ 400 a 450, a diferença não compensa. **Vamos usar tablet ou celular Android.**
- O ESP32 só volta a ser considerado com volume (300 unidades ou mais), placa própria a cerca de R$ 200 e contratos fechados.
- O servidor deve aceitar qualquer aparelho: HTTP e WebSocket, ou MQTT. Assim, trocar o aparelho no futuro não obriga a refazer o resto.

### A-02: a Fase 1 não tem terminais nas mesas
- O lançamento é **no caixa** e no **tablet ou celular do garçom**, que anota o pedido na mesa (como os palmtops de antigamente).

### A-03: dois modos de lançar o pedido, na mesma comanda
| Modo | Como funciona |
|---|---|
| **Cardápio** (tradicional) | O garçom navega pelas categorias, toca no produto e escolhe complementos e observações |
| **Assistente de Pedido** (rápido) | Por voz, item por item (ver A-04) |
- O garçom pode trocar de modo no meio do pedido.
- Sem internet, o Assistente fica indisponível e o Cardápio continua funcionando. A comanda não se perde.
- O nome oficial é **"Assistente de Pedido"**, inspirado nos assistentes de redação.

### A-04: como funciona o Assistente de Pedido
1. O garçom escolhe a **mesa**.
2. Escolhe **Cardápio** ou **Assistente de Pedido**.
3. O cliente fala. O garçom **segura o botão, repete o item e solta**. O item aparece na lista em 1 a 2 segundos. Isso se repete para cada item.
   - A fala também pode mudar o que já foi anotado: "o X-salada de antes é com ovo", "mais uma", "tira a Coca".
4. "Mais alguma coisa?" "Não." O garçom toca em **Revisar pedido**. O nome do botão ainda pode mudar; o William falou em "pedido total".
5. O garçom lê a lista para a mesa.
   - Se algo precisar mudar, ele **toca no item, segura o botão e fala a correção** em linguagem natural ("esse é normal, sem ovo"). Depois revisa de novo e lê de novo.
6. Toca em **Enviar**. O pedido é separado por setor e vai para a impressora de cada setor (cozinha, bar...) com o número da mesa.
7. O garçom fica livre para atender outra mesa.

**Regras do Assistente**
- O garçom repete o pedido. O sistema **não grava a conversa da mesa**, o que melhora a precisão e evita problema com a LGPD.
- O botão é de **segurar para falar**. Há uma fila de falas, aplicadas na ordem em que foram ditas, e um botão de **desfazer a última**.
- Com um item selecionado, "esse" passa a ser aquele item.
- **Cada unidade é guardada em separado.** A tela só junta as unidades iguais para facilitar a leitura. "Um deles é sem ovo" divide a linha.
- O sistema só escolhe produtos que existem no cardápio. Se houver dúvida, a linha aparece em amarelo com as opções mais próximas, ou o sistema pergunta qual item.
- Cada produto pode ter **sinônimos e apelidos** cadastrados ("uma zero", "X-tudo"). O sistema aprende com as correções.
- Correções que não fazem sentido para o item, como "sem gelo" num lanche, não são aplicadas, e a tela mostra um aviso.
- Componentes técnicos: transcrição de fala em português (Whisper ou equivalente) e um modelo de linguagem que transforma a frase em operações sobre a comanda (acrescentar, alterar, trocar, quantidade, remover, dividir). O custo previsto é de poucos centavos por pedido (estimativa, a confirmar).

### A-05: envio e impressão
- Cada produto tem um **setor de impressão** cadastrado.
- Impressora térmica de 80 mm, comandos ESC/POS, **de preferência ligada por cabo de rede**.
- O tablet mostra **"Enviado: cozinha ✓ bar ✓"** quando cada impressora confirma. Se uma falhar, o garçom e o caixa recebem um alerta, e o pedido fica numa fila até ser impresso.
- Opção **"Enviar bebidas agora"**, que manda só a parte do bar antes do resto.
- Um pedido feito depois na mesma mesa entra como **novo pedido na mesma comanda**: a cozinha recebe só o que é novo.

### A-06: gestão básica (ter em mente na implementação)
O William pediu para lembrar disto ao implementar o sistema:
- **Fechamento de caixa.**
- **Relatório do dia por setor:** bebidas, lanches e outros, com quantas unidades saíram de cada item.
- **Estimativa de consumo de ingredientes**, a partir da ficha técnica de cada produto.
- **Módulo de estoque** aproximado.
- O sistema deve ficar aberto para outras ferramentas de gestão.

**Consequência para o banco de dados, desde o início:** cada item vendido fica registrado com produto, setor, complementos, mesa, garçom, horário e situação. Produto e ingrediente se ligam por ficha técnica. Assim os relatórios e o estoque são só consultas e telas novas, e não exigem refazer o banco.

---

## 3. Pontos em aberto

- **Nota fiscal (NFC-e):** se o caixa fechar contas, precisa emitir nota. Há dois caminhos: integrar com o sistema de caixa que o restaurante já usa (recomendado para começar) ou emitir pela própria plataforma, com uma API fiscal paga (Focus NFe, PlugNotas ou similar). **Ainda não decidido.**
- **Equipamentos:** o William vai escolher tablets, impressoras e o resto e mandar a configuração para avaliação. Checklist do que conferir:
  - **Tablet ou celular:** Android 10 ou mais novo, 3 GB de RAM ou mais (4 GB é melhor), Wi-Fi de 2,4 e 5 GHz, bateria para um turno, bom microfone, homologação ANATEL.
  - **Impressoras:** térmica de 80 mm, ESC/POS, cabo de rede, guilhotina; na cozinha, resistência a calor e gordura.
  - **Servidor:** mini PC dedicado com nobreak, em vez do computador do caixa.
  - **Rede:** ponto de acesso profissional que cubra o salão, e internet estável (o Assistente depende dela).
  - **Restaurante do piloto:** quantos garçons, mesas e setores de impressão.
- **Aparelho do garçom:** celular simples, tablet de 8" ou maquininha Android com impressora (Sunmi, PAX).
- **Repositório próprio** para o sistema: ainda não criado.

## 4. Mercado (pesquisa de 31/10/2026)

- **No Brasil**, os sistemas de comanda eletrônica (Saipos, Consumer, Goomer, Colibri, Linx e outros) funcionam por toque. Não encontramos comanda por voz para o garçom como produto pronto. Há uma vaga no Workana (06/2026) pedindo exatamente isso, o que mostra interesse e possíveis concorrentes começando agora.
- **Lá fora**, a voz com IA em restaurante atende o **cliente**: pedido por telefone e drive-thru (SoundHound, ConverseNow, VOICEplug, Aldelo) e pedido feito pelo cliente na mesa (TableVoice).
- **Diferencial:** português de verdade, apelidos do cardápio local, boa confirmação e integração com o caixa e as impressoras. O espaço existe, mas por pouco tempo.

## 5. Próximo passo

1. Receber e avaliar a lista de equipamentos do William.
2. Escrever a especificação da Fase 1: telas, fluxo, comandos de voz, regras de impressão, comportamento sem internet e banco de dados já pensado para a gestão (A-06).
3. Criar o repositório próprio e mover esta pasta para lá.
