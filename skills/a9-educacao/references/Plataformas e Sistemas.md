# Plataformas e Sistemas

Padrão A9 de interface e experiência de uso · revisado em 29/10/2026

Use este guia para construir plataformas, CRMs, painéis, ferramentas internas e seus formulários. A identidade visual está em [Design System](Design%20System.md), com fontes, logos e tokens já incluídos na skill. Sites institucionais e apresentações seguem as referências próprias dessas superfícies.

## Base e alcance

Este guia adapta o [arquivo publicado no CRM](https://crm.a9p.com.br/paginas/skill-ia-a9-design-system-para-criacao-de-plataformas), comparado com os componentes e telas do CRM em 29/10/2026. A base visual e os padrões de autocomplete, máscaras, CRUD e paginação permanecem compatíveis. Esta revisão explicita os switches, detalha os calendários atuais e corrige a diferença entre recomendação e valor padrão de componente.

Para novas interfaces A9, aplique as escolhas deste guia. O CRM contém exceções e telas anteriores, inclusive checkboxes para seleção de linhas. A existência dessas telas não muda o padrão solicitado para novas construções e não autoriza reformá-las automaticamente.

Em um projeto existente, reutilize os componentes, tokens, rotas e regras de negócio do próprio produto. Confira a implementação atual antes de copiar exemplos. Um pedido explícito do usuário orienta o escopo. A skill não concede acesso ao CRM nem autorização para publicar, enviar mensagens ou alterar dados.

## Base visual e implementação

- Fundo navy, Poppins no corpo e títulos, JetBrains Mono em código e identificadores. Lime e ciano como acentos.
- Use os tokens do pacote. No CRM, reutilize também os tokens semânticos `background`, `card`, `primary`, `border`, `input`, `ring` e suas variantes de tema.
- Preserve o modo claro quando o produto já o oferece. Calendários e popovers acompanham o tema.
- Inputs e botões têm altura base de 40 px e raio base de 8 px. Reutilize variantes compactas existentes quando a densidade da tela exigir.
- Ícones Lucide. Uma ação principal dominante por tela. Gradiente horizontal somente em destaques pontuais.
- Para um projeto novo sem stack definida, a referência é React, TypeScript, Vite, Tailwind, shadcn/Radix, React Router, TanStack Query e Sonner. Preserve outra stack solicitada e traduza os padrões de interação.
- Antes das telas, configure fontes, logos oficiais, tokens, componentes base e app shell. Use os assets locais desta skill. Se um asset necessário faltar, informe a lacuna.

## Escolha dos campos

| Necessidade | Componente do padrão A9 |
| --- | --- |
| Ligar ou desligar, ativo, habilitar, receber avisos, opção sim/não | `Switch` com label associado |
| Escolher um item | `Combobox` com pesquisa |
| Escolher vários itens | `MultiCombobox` com pesquisa e seleções visíveis |
| Data simples | `DatePicker` ou `Input type="date"` do produto, integrados ao `DateInput` no CRM |
| Mês de referência | `Input type="month"` do produto, integrado ao `DateInput` no CRM |
| Data e hora | `DatePicker showTime` |
| Intervalo de datas | `DateRangePicker` |
| Texto, texto longo ou e-mail | `Input`, `Textarea` ou `Input type="email"` |

### Switches

Use Switch em opções booleanas de novos formulários e configurações. Não use checkbox como substituto visual. Para escolher vários responsáveis, categorias ou produtos, use MultiCombobox.

Associe `id` e `Label htmlFor`, controle `checked` com booleano e atualize por `onCheckedChange`. Mostre o estado com texto quando necessário. Desabilite durante a gravação quando a mudança salvar imediatamente, sem permitir envios duplicados.

O componente não define a regra de salvamento. Em um formulário com botão Salvar, a troca altera o estado do formulário. Em uma configuração de efeito imediato, trate loading, sucesso e falha da gravação. Não invente valores iniciais nem obrigatoriedade.

### Seleção com autocomplete

- Use Combobox para seleção única e MultiCombobox para múltipla. Selects simples ficam restritos a listas muito pequenas e fixas já previstas no produto. Para entidades, filtros pesquisáveis e listas que crescem, use autocomplete.
- Para selecionar registros existentes, passe `allowFreeText={false}` explicitamente. O Combobox atual do CRM tem `allowFreeText = true` na implementação. Omitir a propriedade permite texto livre.
- Libere texto livre somente quando o campo admitir valores novos pela regra de negócio.
- Busca remota com debounce de 300 ms, mínimo de 2 caracteres e até 20 resultados por consulta. Busque no backend apenas as colunas necessárias.
- Antes do mínimo, mostre “Digite ao menos 2 caracteres para buscar”. Durante a consulta, “Buscando...”. Sem resultado, use uma mensagem contextual. Mostre falha de consulta como erro, sem confundi-la com lista vazia.
- Use o ID do registro como valor. Preserve o rótulo escolhido quando ele não estiver nos resultados atuais. No Combobox do CRM, `selectedLabel` atende esse caso.
- Diferencie nomes repetidos com complemento relevante e autorizado. Em seleção múltipla, mantenha os itens escolhidos visíveis, com remoção individual e resumo quando houver muitos.
- As props `onSearch` e `loading` não implementam debounce ou consulta sozinhas. A tela ou hook controla a busca. Confira as props disponíveis do MultiCombobox antes de reutilizá-lo.
- Garanta setas, Enter, Escape, foco visível e nome acessível. Não replique lacunas de acessibilidade de componentes existentes.

### Datas e calendários

O CRM tem um DateInput próprio com digitação mascarada e calendário em popover. O Input do produto encaminha `type="date"` e `type="month"` para esse componente. O DatePicker sem horário também usa DateInput. Não troque esses wrappers por um input nativo isolado.

- Data visível em `dd/mm/aaaa`, mês em `mm/aaaa` e horário em 24 horas. Valores de data simples seguem `YYYY-MM-DD` e de mês seguem `YYYY-MM`.
- Preserve datas sem horário como datas civis. Não converta vencimentos ou aniversários para UTC, o que pode deslocar o dia.
- DateInput oferece navegação de mês/ano, calendário pt-BR e atalhos Hoje, +15 dias, +30 dias e Fim do mês para datas completas. Respeite `min`, `max` e `disabledDate`.
- Valide datas impossíveis e períodos não permitidos. Data de nascimento não aceita futuro.
- Para data e hora, o DatePicker atual usa Ant Design, Day.js e locale pt-BR. `showTime` apresenta `DD/MM/YYYY HH:mm` e retorna uma string ISO. Confirme o fuso exigido pelo produto.
- DateRangePicker usa o RangePicker do Ant Design com tema A9, início e fim, limpeza e presets Hoje, Últimos 7 dias, Últimos 30 dias, Este mês, Mês passado e Este ano.
- No wrapper atual, `startValue` e `endValue` recebem datas `YYYY-MM-DD`. `onChange` devolve duas strings nesse formato. Limpar uma ponta devolve string vazia para ela.
- Defina pela regra de negócio se as pontas do intervalo são obrigatórias e valide início menor ou igual ao fim. Os wrappers não definem essa obrigatoriedade.
- Preserve label, erro inline, navegação por teclado e retorno de foco ao fechar o calendário. Confira calendário e popover no celular.

## Formulários, máscaras e retorno

Use labels associados aos campos. Placeholder complementa o label com formato ou exemplo. Indique campos obrigatórios, valide antes de enviar e apresente o erro junto ao campo, com `aria-invalid` e descrição acessível.

| Campo | Apresentação e validação |
| --- | --- |
| Telefone brasileiro | Máscara de fixo/celular, com DDI quando aplicável. Normalize para busca e envio conforme o contrato da API |
| CPF | `000.000.000-00`, 11 dígitos, validação dos dígitos verificadores e rejeição de sequências repetidas |
| CNPJ | Reutilize o formatador e validador vigente no produto. No fluxo numérico atual, `00.000.000/0000-00` e dígitos verificadores |
| CEP brasileiro | `00000-000`, consulta ao completar 8 dígitos, preenchimento de endereço e alternativa manual em caso de falha |
| Endereço no exterior | Campos manuais e código postal conforme país. Não aplicar máscara brasileira |
| E-mail | `type="email"`, validação e checagem de duplicidade no backend quando único. Sem máscara visual |
| Moeda | `1.234,56`, representação consistente em centavos e exibição com `Intl.NumberFormat("pt-BR")` |

Campos de estado e cidade usam seleção pesquisável quando houver base disponível. Consultas de CEP ou cadastro não dispensam revisão do usuário. Não escolha provedores externos nem envie dados a eles sem necessidade do fluxo autorizado.

Ações mostram loading, estado desabilitado quando aplicável, feedback de sucesso e erro legível. Botões de envio mudam para “Salvando...” ou equivalente. Preserve o que a pessoa digitou em caso de falha. Toda ação apenas com ícone tem nome acessível e tooltip. Não esconda erro somente no console.

## Estrutura, CRUD e confirmação

- App shell com sidebar recolhível no desktop, Sheet no celular, header e conteúdo operacional. Sistemas não precisam de hero de marketing.
- Lista com título, contexto ou contador, filtros e ação principal. Formulários em largura contida, com seções claras. Evite card dentro de card.
- Criação e edição de entidade principal usam telas próprias. Dialog fica para cadastro auxiliar contextual, configuração curta, exportação ou tarefa em etapas.
- Rotas de referência são `/entidades`, `/entidades/novo`, `/entidades/:id` e `/entidades/:id/editar`. Preserve as rotas reais do projeto.
- Ao criar, abra o detalhe da entidade. Ao editar, volte ao detalhe ou siga o fluxo de sucesso do produto. Invalide as consultas afetadas.
- Exclusão usa AlertDialog com consequência concreta e botão destrutivo com loading. Não use `window.alert` ou `window.confirm`. Imprimir ou exportar, por si só, não exige confirmação destrutiva.
- Reutilize o soft delete e a auditoria quando previstos no produto. Permissões precisam ser aplicadas no backend, além da interface.
- URLs públicas têm slug estável, único, sem acentos e com hífens. Alterar o título não deve quebrar o endereço publicado.

## Tabelas, filtros e paginação

- Paginação no backend para bases grandes. Referência inicial de 20 itens por página. Preserve o tamanho configurado na tela existente.
- Ordenação com lista permitida de colunas e critério estável. Busque somente as colunas necessárias.
- Busca com debounce de 300 ms. Alterar filtros retorna à página 1. Mostre filtros ativos e opção de limpar.
- URLs usam parâmetros curtos, como `page`, `de` e `ate`. Omita `page=1`. Filtros extensos usam o mecanismo do produto, sem JSON/base64 gigante na URL.
- Contagem pode ser separada da consulta de linhas. Se for estimada, indique isso e não a apresente como total exato. Prefira agregações no backend para indicadores grandes.
- Preserve o contexto durante refetch. Use cache, cancelamento e invalidação do TanStack Query conforme a necessidade. Não imponha um único retry ou staleTime a todas as telas.
- Estado inicial, atualização, vazio e erro têm mensagens distintas. Nunca carregue a base inteira só para paginar no navegador.
- Ações da linha ficam no fim, com tooltip e nome acessível. Datas, telefone, documentos e moeda aparecem formatados.
- Paginação mostra os itens e a posição atual, com Anterior e Próximo desabilitados nos limites. Reutilize salto direto de página quando disponível.

## Responsividade e revisão

Formulários de duas colunas viram uma no celular. Filtros e botões podem quebrar linha. Tabelas largas têm rolagem horizontal. Dialogs cabem na viewport, com limite de altura e rolagem interna. Não corte labels, erros, calendário ou ações.

Antes de entregar, confira os campos booleanos, seleções única e múltipla, pesquisa remota, datas, período, máscaras e erros. Teste teclado, foco, carregamento, ausência de resultados, falha ao salvar e as larguras de celular e desktop. Confira contraste e estados por texto ou ícone além da cor. Aplique apenas os testes pertinentes à mudança.

## Referências técnicas verificadas

Código do CRM na revisão `f8fbd26600d069ec1370b3a2a8860d58aca9c37e` da main, consultada em 29/10/2026. Estes caminhos são para localizar a implementação quando houver acesso ao repositório, não dependências do pacote.

- `src/index.css` e `src/components/ui/button.tsx` para tokens e botões.
- `src/components/ui/switch.tsx`, `combobox.tsx` e `multi-combobox.tsx` para seleções.
- `src/components/ui/input.tsx`, `date-input.tsx`, `date-input.css`, `date-picker.tsx` e `calendar.tsx` para datas e tema.
- `src/pages/ContactCreatePage.tsx` e `ContactEditPage.tsx` para switches, autocomplete, máscaras e data de nascimento.
- `src/pages/ContactsPage.tsx`, `CompaniesPage.tsx` e `src/components/AppSidebar.tsx` para listas e navegação.

Os exemplos e valores acima orientam a construção. Não são comprovação de que todas as telas históricas do CRM já foram padronizadas.
