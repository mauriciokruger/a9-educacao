# Validação do guia de plataformas

Revisão de 29/10/2026 para a versão 1.2.0.

## Comparação com o CRM

O arquivo obtido pelo iframe da [página indicada](https://crm.a9p.com.br/paginas/skill-ia-a9-design-system-para-criacao-de-plataformas) foi comparado com o guia do repositório e com a main do CRM na revisão `f8fbd26600d069ec1370b3a2a8860d58aca9c37e`. A consulta foi somente de leitura. Não foram alterados o arquivo publicado, as telas do CRM ou dados operacionais.

| Tema | Evidência e tratamento |
| --- | --- |
| Cores, fontes e componentes | Navy, lime, ciano, Poppins, JetBrains Mono e componentes semânticos continuam alinhados ao guia |
| Switches | Existem em configurações e no cadastro de contatos. O arquivo original não detalhava seu uso. A nova referência explicita Switch para booleanos conforme o pedido |
| Checkboxes | Ainda existem no CRM, inclusive em presença e seleção de linhas. A revisão documenta essa diferença e não apresenta o CRM inteiro como já padronizado |
| Autocomplete | Combobox, MultiCombobox e busca de empresa com 300 ms, 2 caracteres e limite de 20 confirmados. Seleção de registro exige `allowFreeText={false}`, pois o componente tem valor padrão verdadeiro |
| Calendários | Input de data e mês passa por DateInput próprio. DatePicker sem horário também. Data e hora e intervalos usam Ant Design com tema A9. A nova referência cobre os dois caminhos |
| Listas e CRUD | Mantidos telas próprias, filtros, paginação no backend, feedback e componentes de confirmação |
| Ajustes de orientação | Configurações de cache, contagem e retry passam a depender da tela. Impressão e exportação deixam de ser tratadas como motivo automático de confirmação destrutiva |

As fontes de componentes base estavam iguais entre o checkout local e a main consultada. O cadastro de contatos recebeu mudanças em outros campos, e sua versão atual na main foi consultada para confirmar Switch, DatePicker e autocomplete. Componentes recentes de Financeiro também mostram variantes compactas, preservadas pela orientação de reutilizar o produto existente.

## Testes

Uma avaliação independente usando apenas a skill anterior concluiu que checkbox e select nativo não violavam uma regra documentada. Switch, Combobox, MultiCombobox e calendários eram escolhas por suposição. Isso confirmou a lacuna da referência distribuída.

O contrato de distribuição foi ampliado antes da integração e falhou pela ausência do guia na pasta e no ZIP. Depois da inclusão, a suíte completa passou com seis testes, incluindo integridade do arquivo, fontes, modelos de apresentação e e-mail e PDF existente. A construção também valida as referências internas do pacote.

A avaliação independente repetiu o pedido com a referência revisada e selecionou Switch nos dois booleanos, Combobox para cliente, MultiCombobox para responsáveis, DateInput/DatePicker para vencimento e DateRangePicker para período. Aplicou os limites de busca, a desativação explícita de texto livre e o tratamento de datas civis sem UTC. Não foram identificadas contradições impeditivas. A revisão final também explicitou o contrato de valores de início e fim do DateRangePicker.

Esta validação cobre a documentação e sua distribuição. Não é um teste funcional de todas as telas do CRM nem uma nova validação visual dos modelos que permaneceram iguais.
