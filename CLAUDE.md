# Portais Públicos — Secke Sistemas

**Antes de qualquer trabalho, leia [PASSAGEM.md](PASSAGEM.md).** William alterna entre duas contas do Claude. O `PASSAGEM.md` diz o que foi feito, onde está cada coisa e qual é o próximo passo.

**Ao terminar a sessão** (ou quando o limite estiver perto), atualize o `PASSAGEM.md`: uma entrada nova no topo do "Diário das sessões" e o "Estado atual" revisado. Depois, faça commit e push.

- O código do portal e do painel fica no repositório `willquerubim2025-oss/portal-municipal`. Siga o `CLAUDE.md` de lá: decisões em `docs/06-decisoes.md` e pendências em `docs/07-pendencias.md`.
- **Jeriquara está fora do projeto (D-82):** a dispensa não foi ganha. Não testar, conferir nem planejar nada para Jeriquara. Nas instruções, passo a passo, exemplos e respostas ao William, não citar Jeriquara: usar a SMEDU ou um exemplo genérico. O produto é multi-organização; a organização em foco é a SMEDU de Paulínia.
- **Pendências com a SMEDU:** tudo o que depende da Secretaria ou da Prefeitura vai para `docs/reuniao/smedu-pendencias.md`. Enquanto a resposta não chega, não parar: usar dado público, foto de banco com licença livre ou placeholder, marcar no documento o que ficou provisório e seguir. Só parar e cobrar se a falta travar o trabalho.
- Este repositório guarda a especificação, o contexto, o design, as prévias e os documentos de reunião do Portal Educação Paulínia.
- **Manuais e guias (D-135 do `portal-municipal`):** a experiência do usuário é o centro, como nos sistemas. Modelo: o Guia do Usuário da CI (`ci-eletronica/docs/guia/`): uma unidade por papel, índice no início, "Problemas e o que fazer" no fim, fotos reais com números, fluxogramas e cartões; gerado por código para ser refeito quando as telas mudarem.

## Materiais de apresentação e guias (D-137)
Apresentação impressa e Guia do Usuário de qualquer sistema seguem o molde aprovado: receita em `portal-municipal/docs/13-padrao-materiais.md` (modelos: `Portais-Publicos/docs/portfolio/apresentacao/` e `ci-eletronica/docs/guia/`). Começar copiando a pasta `fonte/` do modelo. Na apresentação, primeiro conquistar; a técnica vem no fim.
