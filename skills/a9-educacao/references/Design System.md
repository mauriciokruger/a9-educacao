# Design System

Identidade A9 Educação · pacote 1.2.0 · referência visual A9 v2.0 de maio de 2026

## Princípios

Use fundos escuros nas apresentações e peças digitais. O azul navy forma a base, com lime e ciano nos destaques. Para propostas, contratos e impressão, prefira fundos claros que facilitem a leitura.

O design system oficial define nossa identidade. Os padrões atuais do CRM complementam a experiência de sistemas. Materiais antigos ajudam a entender composição, mas não substituem as fontes e cores daqui.

Um pedido explícito do usuário ou seu modelo de referência orienta a entrega. Não impor a marca A9 a trabalhos de outras empresas.

## Cores

| Token | Valor | Uso |
| --- | --- | --- |
| a9-lime | #6DFF30 | CTA, sucesso, foco e destaque |
| a9-lime-pure | #00FF00 | Variante de marca e line-art |
| a9-cyan | #29FFE8 | Informação, links e detalhes |
| a9-cyan-pure | #00FFE7 | Variante de marca |
| a9-navy-deepest | #03081C | Capas, fechamentos e base mais escura |
| a9-navy-900 | #050E2A | Fundo principal |
| a9-navy-800 | #0A1638 | Cards |
| a9-navy-700 | #122150 | Hover e separadores |
| a9-navy-600 | #1E2F6A | Bordas |
| a9-navy-ink | #04102B | Navy da marca |
| a9-fg-1 | #FFFFFF | Títulos em dark |
| a9-fg-2 | rgba(255,255,255,0.78) | Corpo em dark |
| a9-fg-3 | rgba(255,255,255,0.55) | Metadados |
| a9-fg-4 | rgba(255,255,255,0.30) | Decoração e desabilitado |
| a9-fg-on-lime | #03081C | Texto em lime |
| a9-paper | #F6F7FB | Fundo claro |
| a9-paper-2 | #ECEEF6 | Superfície clara secundária |
| a9-ink-1 | #03081C | Texto principal claro |
| a9-ink-2 | #2A3050 | Texto secundário claro |
| a9-ink-3 | #5A6086 | Metadados claros |
| a9-success | #6DFF30 | Sucesso |
| a9-info | #29FFE8 | Informação |
| a9-warn | #FFB84A | Atenção |
| a9-error | #FF5A5F | Erro ou destrutivo |

O gradiente da marca vai de #6DFF30 a #29FFE8, na direção horizontal. Usar em uma ou duas palavras-chave, número de destaque ou barra fina. Evitar corpo de texto e fundos inteiros em gradiente.

Não usar lime como texto pequeno sobre branco. Em materiais claros, usar navy para textos e lime como superfície ou acento. Estados precisam de rótulo ou ícone além da cor.

## Tipografia

| Papel | Fonte | Pesos |
| --- | --- | --- |
| Títulos e corpo | Poppins | 400, 500, 600, 700 e 900 |
| Código, identificadores e números técnicos | JetBrains Mono | 400 e 600 |

Os arquivos locais estão em assets/fonts. Use-os para HTML offline e em ferramentas que aceitem fontes locais. Em programas que dependem das fontes instaladas, orientar a instalação antes de apresentar ou editar.

Se Poppins não carregar, as alternativas técnicas são Montserrat, system-ui, Segoe UI e sans-serif. Para a fonte mono, use ui-monospace, Consolas ou monospace. Fallback não é escolha visual para a entrega final. Não substituir silenciosamente por Arial, Inter, Roboto, Manrope ou Space.

A escala digital usa os tamanhos 13, 15, 17, 20, 24, 32, 44, 60, 84 e 112 px. Corpo usual em telas de leitura entre 15 e 17 px. Títulos de sistemas entre 24 e 32 px. Slides usam escala própria descrita no guia de apresentações.

Entrelinha de corpo entre 1,45 e 1,6. Títulos entre 1,05 e 1,15. Textos longos alinhados à esquerda e em fg-2 no dark. Números comparáveis usam tabular-nums.

## Espaçamento, raios e efeitos

O espaçamento segue uma base de 4 px. Use 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96 ou 128 px.

Os raios são de 4, 8, 14, 20, 28 ou 40 px. Para botões em formato de cápsula, use 9999 px. Em sistemas, campos e botões usam 8 px. Ajuste os cards à quantidade de conteúdo. Em peças editoriais, cards podem usar 20 a 24 px e botões pill.

Sombras e glows estão nos tokens. Usar glow com moderação, no elemento âncora. Não criar efeito em todo texto ou componente.

Movimento rápido de 140 ms, base de 240 ms e entrada de 480 ms. Usar ease-out cubic-bezier(0.16,1,0.3,1). Respeitar prefers-reduced-motion.

## Logo

Use os PNGs oficiais a9-branco.png, a9-preto.png e a9-colorido.png. Escolha a logo branca para fundos navy e a preta para fundos claros. A colorida funciona quando houver contraste suficiente.

Preservar proporção, transparência e área de respiro. Não recriar, distorcer, recolorir ou gerar a marca com IA. Não usar texto A9 como substituto da logo. Não colocar sobre fotografia sem contraste suficiente.

A extensão SVG não garante um vetor. Usar SVG apenas quando for um arquivo vetorial oficial confirmado. Os PNGs oficiais deste pacote são a referência disponível, em resolução original.

## Sites e landing pages

Grid com largura máxima de 1280 px e padding lateral de 24 px no desktop e 16 px no celular. Usar título, contexto curto, benefício concreto, conteúdo e um próximo passo dominante.

Hierarquia clara, pouco texto por bloco e imagens com função. Usar prova social apenas quando fornecida e autorizada. Não inventar depoimentos, clientes, datas, lotação ou preços.

Botão principal lime com texto navy. Contraste, foco visível, navegação por teclado, labels e textos alternativos são parte da entrega.

## Sistemas e ferramentas internas

Para construir plataformas, CRMs, painéis, formulários e componentes, leia [Plataformas e Sistemas](Plataformas%20e%20Sistemas.md). O guia detalha switches, seleções com autocomplete, calendários, máscaras, rotas, filtros e paginação, com revisão do código do CRM em 29/10/2026.

Interfaces do CRM usam Poppins, tokens navy e componentes consistentes. Para novos sistemas, React, TypeScript, Tailwind, shadcn/Radix e Lucide são referências de implementação quando o usuário não tiver escolhido outra stack.

- App shell com sidebar, header e área de conteúdo. No celular, navegação recolhível.
- Tabelas e formulários priorizam leitura e execução. Evitar hero em tela operacional.
- Ações têm loading, estado desabilitado, retorno legível e erro contextual.
- Inputs têm label, validação e formato adequado. Campos monetários e datas usam pt-BR.
- Ícones de ação têm nome acessível e tooltip.
- Cadastro e edição de entidades principais usam telas próprias. Reserve os modais para tarefas auxiliares.
- Confirmar exclusões no componente da interface com explicação do impacto.
- Listas grandes usam busca com debounce e paginação no backend. Não carregar uma base inteira apenas para paginar no navegador.
- Usar a infraestrutura de acesso do produto. A skill não implementa nem substitui permissões.

Essas são orientações para construir interfaces, sem autorização para conectar ou alterar o CRM.

## Documentos, propostas e impressão

Preferir fundo claro e texto navy para documentos de leitura e impressão. Formato A4, margens de 25 mm laterais e 22 mm no topo e rodapé. Poppins 12 pt no corpo, títulos de seção entre 18 e 24 pt.

Propostas separam objetivo, escopo confirmado, formato, cronograma e condições fornecidas. Valores ou datas ausentes ficam pendentes. Contratos usam composição sóbria, sem gradientes decorativos.

Tabelas conservam unidade, período e origem. Não usar screenshots como substituto de tabelas que precisam continuar editáveis.

## E-mail

Use o [guia de e-mails e assinaturas](E-mails%20e%20Assinaturas.md) e o modelo em assets/emails/modelo-a9.html. O padrão tem cabeçalho navy com a logo branca, detalhe lime, corpo claro e um botão principal. A largura máxima é de 600 px.

Use parágrafos curtos e inclua a assinatura com foto no final por padrão. Preserve a assinatura já configurada de quem está escrevendo. A pessoa pode pedir para removê-la.

Poppins pode não carregar em alguns programas. Declare Arial, Helvetica e sans-serif como alternativas. Use tabelas e estilos no próprio elemento para manter a compatibilidade. Confira as imagens na mensagem salva.

## Redes sociais

Usar o formato solicitado. Como referência, feed em 1080 × 1350 e story em 1080 × 1920, com área segura e texto legível. Um card desenvolve uma ideia. Quantidade de cards segue o pedido e o conteúdo.

Não converter automaticamente um modelo pessoal ou de um produto em regra universal da A9. Capa, títulos e rodapé de um modelo aprovado devem ser preservados quando esse modelo for solicitado.

## Apresentações

Seguir o guia Apresentações.md. O padrão é HTML navegável 16 por 9, usando o modelo autocontido incluído. Slides têm ritmo editorial e não recebem automaticamente o layout de um dashboard.

## Recursos e procedência

O arquivo assets/tokens/tokens.json reúne os valores usados no código. O comando de construção gera tokens.css a partir dele. Confira os valores deste guia antes de publicar uma versão.

A identidade segue o [Design System oficial A9 v2.0](https://drive.google.com/file/d/14XdmHQ5KyhP0jPc9pCB_1vt9IkDqtkhj/view) e padrões de interface do CRM A9 consultados em 27/10/2026. Os materiais existentes foram usados somente como referência de composição, sem transportar dados operacionais.
