# SMEDU · dados a confirmar

Carga inicial feita em 12/10/2026 na homologação, a partir de fontes públicas. A fonte principal foi a página da Secretaria de Educação em www.paulinia.sp.gov.br, atualizada em 04/09/2026. Cada unidade tem `legado.confirmar = true` no banco.

Cada item traz: o que precisamos · onde será usado · o que muda conforme a resposta · se bloqueia.

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
- **Onde será usado:** página Matrícula Escolar. Hoje ela mostra o ciclo de 2026 e avisa que o de 2027 será publicado.
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
- **Onde será usado:** seção Equipe gestora na home e na página Estrutura organizacional. As duas estão vazias hoje. O card "Secretaria de Educação" leva à Estrutura organizacional.
- **O que muda:** a seção aparece quando houver nomes.
- **Bloqueia?** Não. Fica oculta enquanto vazia.

## 8. Páginas obrigatórias do rodapé: Acesso à Informação, Ouvidoria e Privacidade
- **O que precisamos:**
  - **Acesso à Informação e e-SIC (Lei 12.527/2011):** o link do pedido eletrônico de informação da Prefeitura (o e-SIC atende a Secretaria ou ela tem canal próprio?), endereço e horário do atendimento presencial, prazos e como recorrer;
  - **Ouvidoria (Lei 13.460/2017):** o canal da Ouvidoria que atende a Educação (link, e-mail, telefone e endereço) e se a Secretaria tem ouvidor próprio;
  - **Privacidade (LGPD, Lei 13.709/2018):** nome e e-mail do encarregado de dados (DPO) da Prefeitura e, se existir, a política de privacidade oficial para seguirmos o mesmo texto.
- **Onde será usado:** links do rodapé de todas as páginas (Acesso à Informação, Ouvidoria, Privacidade) e o card "Ouvidoria" dos Serviços.
- **O que muda:** hoje essas três páginas estão em rascunho e os links do rodapé abrem "página não encontrada". Com os dados, escrevemos e publicamos as três. A página de **Acessibilidade** já foi escrita e publicada na homologação em 15/10/2026, com o e-mail e o telefone da Secretaria (confirmar se são esses os canais para relatar problemas).
- **Bloqueia?** Não para a homologação; **sim antes de ir ao ar** (são exigências legais e entram na avaliação do PNTP).
