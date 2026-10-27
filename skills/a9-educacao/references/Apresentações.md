# Apresentações

## Formato e preparação

Sem formato especificado, criar apresentação HTML navegável. Usar o modelo em assets/apresentacoes/modelo-a9.html e a demonstração de oito slides como referência de composição.

Identificar público, objetivo, duração e dados disponíveis. Respeitar o número total de slides pedido, incluindo capa quando fizer parte da sequência. Não impor oito slides a outros pedidos e não adicionar capa a um pedido de slide único.

Escrever primeiro a ideia central de cada slide. Reduzir texto antes de reduzir fonte. Separar explicações extensas em notas ou material de apoio quando necessário.

## Identidade

- Canvas de referência de 1920 × 1080, proporção 16 por 9.
- Margem lateral de 96 px, topo de 56 px e rodapé de 36 px.
- Poppins para títulos e corpo. JetBrains Mono somente em códigos e identificadores.
- Títulos de conteúdo entre 44 e 60 px, capa entre 60 e 84 px e corpo entre 24 e 32 px. Texto editorial não deve ficar abaixo de 24 px no canvas de referência.
- Navy como base, branco para títulos, fg-2 para corpo, lime e ciano como acentos.
- Gradiente em uma ou duas palavras-chave ou no dado principal.
- Logo branca no canto inferior direito de slides de conteúdo. Capas, divisórias e encerramento usam a composição própria, sem adicionar uma marca concorrente.
- Numeração discreta e consistente.

Ao exportar para PPTX, manter a proporção e converter medidas do canvas proporcionalmente. Pixels e pontos não são unidades intercambiáveis.

## Tipos de slide

| Tipo | Composição |
| --- | --- |
| Capa | Assunto claro, contexto curto, destaque em uma palavra e respiro |
| Divisória | Capítulo e título, com poucos elementos |
| Conteúdo | Uma ideia com exemplo, imagem ou explicação curta |
| KPI | Número principal, unidade, período e interpretação com fonte |
| Comparação | Dois cenários com critérios equivalentes |
| Gráfico | Eixos, unidades e rótulos legíveis. Destaque no dado importante |
| Citação | Trecho curto com autoria e origem verificadas |
| Encerramento | Próximo passo coerente com o objetivo da apresentação |

Na demonstração do pacote, números e falas estão identificados como fictícios. Não reutilizá-los como fatos.

## Interação no HTML

Manter botões Anterior e Próximo, indicador atual/total e acesso ao slide por índice. Setas, PageUp/PageDown, espaço, Home e End navegam. F ativa tela cheia. O botão visível oferece a mesma ação. Esc sai pelo navegador.

Não capturar atalhos quando o foco estiver em input, textarea, select ou conteúdo editável. Anunciar mudança de slide de forma acessível sem transformar todo o slide em região de leitura automática.

Os controles permanecem acessíveis no celular e não cobrem conteúdo. Em telas estreitas, priorizar leitura, permitindo apresentação em fluxo com o slide ativo. O modo de projeção conserva 16 por 9.

Fontes e logo incorporadas evitam dependência de internet. Remover links externos de fontes, scripts ou bibliotecas ao produzir um HTML offline. Usar imagens locais ou incorporadas com origem autorizada.

## Impressão e PDF

O botão Salvar PDF / imprimir abre a impressão do navegador. Escolher Salvar como PDF, orientação paisagem, gráficos de segundo plano ativados e cabeçalhos/rodapés do navegador desativados.

O CSS de impressão exibe todos os slides, um por página, remove controles e animações e elimina a escala usada na tela. A exportação precisa ter a mesma quantidade de páginas da apresentação.

Conferir a impressão antes de entregar. Um PDF de apenas o slide ativo é um erro.

## PowerPoint editável

Quando o pedido for PPTX, entregar PPTX com textos, tabelas, gráficos e formas de conteúdo editáveis. Usar a ferramenta de apresentações disponível na plataforma. Não converter cada slide em uma imagem como solução padrão.

Instalar Poppins e JetBrains Mono no ambiente de edição. Incorporar fontes quando a ferramenta e suas permissões permitirem. Conferir novamente se outro programa substituir a fonte.

Sem ferramenta capaz de gerar PPTX, informar a limitação e combinar alternativa com o usuário. Não entregar HTML dizendo que é PowerPoint.

## Google Slides

Quando solicitado, usar as ferramentas autorizadas de Google Slides/Drive e manter textos e gráficos editáveis. Usar Poppins. Para detalhes mono, verificar disponibilidade de JetBrains Mono antes de aplicar, comunicando qualquer substituição necessária.

Criar ou alterar um arquivo no Drive depende da autorização e das ferramentas disponíveis na conta. A skill instalada não fornece essa conexão.

## Conferência

1. Quantidade e ordem dos slides correspondem ao pedido.
2. Todas as fontes e logos carregam.
3. Texto não corta nem se sobrepõe em desktop ou celular.
4. Dados, unidades, períodos e fontes estão corretos.
5. Teclado, botões, tela cheia e retorno funcionam.
6. Foco é visível e o modo de movimento reduzido funciona.
7. PDF contém todos os slides, na ordem, sem controles.
8. O arquivo HTML offline continua funcionando com a rede bloqueada.

## Pedido copiável

Use a skill A9 Educação para criar uma apresentação de [N] slides sobre [TEMA], para [PÚBLICO], com o objetivo de [OBJETIVO]. Use os dados [ARQUIVOS OU TEXTO]. Entregue em HTML navegável e prepare a impressão em PDF. Não invente números, datas ou depoimentos.
