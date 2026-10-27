# Prompts por Setor

Biblioteca de aplicação para a rotina da A9 Educação. Os grupos abaixo organizam exemplos de uso; não representam um organograma oficial. Cada comando produz uma proposta ou rascunho para conferência.

Substitua os campos entre colchetes e forneça apenas os dados autorizados. A skill não conecta sistemas nem envia mensagens. Para criar peças visuais, acrescente o formato desejado; apresentações sem formato usam HTML navegável.

## Comercial

### 1. Preparação de conversa

**Objetivo** — organizar uma reunião com contexto.

**Entradas** — resumo autorizado do contato, objetivo e informações disponíveis.

```text
Use a skill A9 Educação. Prepare uma conversa de [DURAÇÃO] com
[PERFIL DO INTERLOCUTOR] sobre [TEMA]. Contexto autorizado [CONTEXTO].
Organize o que sabemos, o que falta confirmar e cinco perguntas
abertas. Termine com um próximo passo sugerido. Não invente dores,
orçamento, interesse ou promessa de resultado.
```

**Saída esperada** — roteiro curto com fatos, perguntas e próximo passo.

**Conferir** — informações atuais, perguntas úteis e ausência de suposições tratadas como fatos.

### 2. Proposta de treinamento

**Objetivo** — estruturar uma proposta com escopo confirmado.

**Entradas** — necessidade, público, entregáveis e condições aprovadas.

```text
Use a skill A9 Educação para preparar uma proposta de [TREINAMENTO]
para [PÚBLICO]. Briefing [BRIEFING]. Condições confirmadas [CONDIÇÕES].
Separe contexto, objetivo, escopo, formato, cronograma e investimento.
Marque como pendente qualquer condição não fornecida. Use documento
claro e legível. Não invente preço, desconto, garantia ou prazo.
```

**Saída esperada** — proposta editável ou conteúdo estruturado no formato pedido.

**Conferir** — escopo, valores e datas contra o briefing.

### 3. Retomada de contato

**Objetivo** — preparar uma mensagem pertinente.

**Entradas** — histórico resumido, canal e próximo passo desejado.

```text
Use a skill A9 Educação. Escreva um rascunho de retomada de até
100 palavras para [PERFIL], pelo canal [CANAL]. Histórico [RESUMO].
Próximo passo desejado [AÇÃO]. Mantenha tom próximo, retome um fato
do histórico e faça um convite simples. Não invente urgência,
disponibilidade, condições ou interesse. Não envie a mensagem.
```

**Saída esperada** — uma mensagem pronta para revisar.

**Conferir** — contexto, destinatário e utilidade do convite.

## Marketing e Conteúdo

### 4. Briefing de campanha

**Objetivo** — transformar informações em direção de conteúdo.

**Entradas** — produto, público, objetivo, canais e condições confirmadas.

```text
Use a skill A9 Educação. Prepare um briefing de campanha para
[PRODUTO OU AÇÃO], com objetivo [OBJETIVO] e público [PÚBLICO].
Informações disponíveis [DADOS]. Entregue mensagem central, benefícios
comprováveis, canais e ideias de peças. Liste lacunas que impedem
publicação. Não invente depoimentos, datas, vagas ou resultados.
```

**Saída esperada** — briefing com mensagem e peças propostas.

**Conferir** — ligação entre público, benefício e evidência.

### 5. Carrossel

**Objetivo** — comunicar uma ideia em sequência.

**Entradas** — assunto, público, quantidade e dados.

```text
Use a skill A9 Educação para criar um carrossel de [N] cards
sobre [TEMA], para [PÚBLICO], no formato [DIMENSÕES].
Base factual [DADOS]. Escreva uma ideia por card, preserve leitura
no celular e termine com uma ação coerente. Use o design system A9.
Se houver modelo aprovado [MODELO], preserve capa, fontes e rodapé.
```

**Saída esperada** — roteiro e arte ou arquivo no formato pedido.

**Conferir** — quantidade, clareza, margens e tamanho da fonte.

### 6. Landing page

**Objetivo** — apresentar uma oferta ou ação.

**Entradas** — briefing, objetivo da página, conteúdo e destino do CTA.

```text
Use a skill A9 Educação para criar uma landing page responsiva de
[AÇÃO]. Público [PÚBLICO]. Informações confirmadas [DADOS].
Objetivo e destino do CTA [OBJETIVO E DESTINO]. Use fontes e logos
oficiais e um próximo passo dominante. Se faltarem datas, preços
ou destino, indique a pendência. Não simule envio de formulário.
```

**Saída esperada** — página ou protótipo funcional conforme pedido.

**Conferir** — contraste, celular, links e funcionamento real do CTA.

## CS e Atendimento

### 7. Boas-vindas

**Objetivo** — orientar os primeiros passos.

**Entradas** — serviço contratado, sequência confirmada e canais.

```text
Use a skill A9 Educação. Prepare um rascunho de boas-vindas para
[PÚBLICO] em [PRODUTO]. Primeiros passos confirmados [PASSOS].
Canais [CANAIS]. Explique o que a pessoa deve fazer agora e onde
buscar ajuda. Não inclua acessos, contatos ou compromissos que não
foram fornecidos. Não envie e não crie contas.
```

**Saída esperada** — orientação curta e checklist de entrada.

**Conferir** — ordem, links e correspondência com o serviço contratado.

### 8. Resposta de atendimento

**Objetivo** — responder com clareza e encaminhamento.

**Entradas** — relato, contexto permitido e orientações vigentes.

```text
Use a skill A9 Educação. Prepare uma resposta para o relato [RELATO].
Contexto autorizado [CONTEXTO]. Orientações confirmadas [REGRAS].
Entregue mensagem de até 120 palavras, informação que falta e
encaminhamento sugerido. Não prometa reembolso, desconto ou prazo
sem confirmação. Não envie a mensagem.
```

**Saída esperada** — resposta revisável e encaminhamento.

**Conferir** — entendimento do problema e compromisso assumido.

### 9. Síntese de retornos

**Objetivo** — encontrar padrões em feedbacks autorizados.

**Entradas** — retornos anonimizados e período.

```text
Use a skill A9 Educação. Analise estes retornos anonimizados
[RETORNOS], do período [PERÍODO]. Agrupe temas, mostre frequência
quando puder contar e selecione três melhorias propostas. Diferencie
percepção relatada de causa comprovada. Não exponha pessoas e não
generalize para toda a base sem amostra suficiente.
```

**Saída esperada** — temas, evidências e melhorias propostas.

**Conferir** — contagem, amostra e preservação de anonimato.

## Educação e Consultoria

### 10. Roteiro de aula

**Objetivo** — organizar aprendizado aplicável.

**Entradas** — tema, público, duração e objetivo.

```text
Use a skill A9 Educação. Prepare uma aula de [DURAÇÃO] sobre
[TEMA], para [PÚBLICO], com objetivo [OBJETIVO]. Base [FONTES].
Organize abertura, explicação, exemplo fictício, prática e conferência.
Respeite a experiência profissional do público. Informe ferramentas
necessárias e adapte a prática ao tempo disponível.
```

**Saída esperada** — roteiro com tempo e atividade.

**Conferir** — viabilidade da prática e entendimento esperado.

### 11. Apresentação de slides

**Objetivo** — criar material para apresentar.

**Entradas** — tema, público, objetivo e fontes.

```text
Use a skill A9 Educação para criar uma apresentação de [N] slides
sobre [TEMA], para [PÚBLICO]. Objetivo [OBJETIVO]. Fontes [DADOS].
Use uma ideia por slide, exemplos identificados e a identidade A9.
Entregue HTML navegável com tela cheia e impressão de todos os slides
em PDF. Não invente estatísticas ou citações.
```

**Saída esperada** — apresentação com slides completos e impressão preparada.

**Conferir** — roteiro, quantidade, tipografia e todas as páginas do PDF.

### 12. Próxima conversa de consultoria

**Objetivo** — preparar orientação a partir do encontro anterior.

**Entradas** — relato autorizado, pendências e objetivo.

```text
Use a skill A9 Educação. Com base no relato [RELATO], prepare
o próximo encontro de orientação sobre [TEMA]. Pendências [LISTA].
Separe fatos, perguntas, prática a orientar e próximos passos propostos.
No Propulsor de IA, deixe claro que a A9 orienta e que o cliente ou
fornecedor escolhido executa e mantém as soluções. Não marque práticas
pendentes como concluídas.
```

**Saída esperada** — guia de conversa e conferência.

**Conferir** — continuidade, pendências e escopo da orientação.

## Eventos e Operações

### 13. Checklist de preparação

**Objetivo** — tornar entregas e pendências visíveis.

**Entradas** — evento, data confirmada, atividades e responsáveis.

```text
Use a skill A9 Educação. Monte um checklist para [EVENTO],
com base em [ATIVIDADES], data confirmada [DATA] e responsáveis
[LISTA]. Organize antes, durante e depois. Mostre dependências e
pendências. Quando não houver responsável ou prazo, marque a definição
necessária. Não considere reservas ou fornecedores confirmados sem fonte.
```

**Saída esperada** — checklist com responsáveis e prazos confirmados ou pendentes.

**Conferir** — dependências, sequência e origem das confirmações.

### 14. Orientação para participantes

**Objetivo** — reduzir dúvidas sobre participação.

**Entradas** — local, horários, acesso e contatos confirmados.

```text
Use a skill A9 Educação. Prepare uma orientação para participantes
de [EVENTO], no canal [CANAL]. Dados confirmados [DADOS].
Explique chegada, horários, o que levar e canal de apoio. Não invente
endereço, estacionamento, alimentação ou condição de acesso.
Entregue rascunho para revisão, sem envio.
```

**Saída esperada** — comunicação objetiva e lista de lacunas.

**Conferir** — data, local, links e condições de acesso.

### 15. Registro de ocorrências

**Objetivo** — organizar aprendizado operacional.

**Entradas** — ocorrências anonimizadas e providências conhecidas.

```text
Use a skill A9 Educação. Organize as ocorrências [REGISTROS]
de [EVENTO]. Para cada tema, separe fato, impacto relatado, providência
registrada e melhoria proposta. Preserve evidências. Não atribua culpa,
causa ou responsabilidade individual sem base. Entregue uma síntese
para reunião de operação.
```

**Saída esperada** — fatos, providências e melhorias.

**Conferir** — distinção entre o ocorrido e a interpretação.

## Financeiro e Administrativo

### 16. Conferência de demonstrativo

**Objetivo** — organizar uma leitura gerencial.

**Entradas** — dados autorizados, período e significado das colunas.

```text
Use a skill A9 Educação. Confira este demonstrativo autorizado
[DADOS], do período [PERÍODO]. Definições [COLUNAS].
Mostre totais, critérios de cálculo, divergências e dados faltantes.
Separe valores previstos de realizados. Não invente lançamentos nem
faça pagamentos ou alterações.
```

**Saída esperada** — resumo com cálculos rastreáveis.

**Conferir** — unidade, período, duplicidades e fórmulas.

### 17. Minuta de cobrança

**Objetivo** — preparar contato respeitoso para conferência humana.

**Entradas** — obrigação confirmada e dados mínimos autorizados.

```text
Use a skill A9 Educação. Prepare uma minuta de cobrança para
[DESTINATÁRIO], sobre [REFERÊNCIA], com saldo confirmado [VALOR]
e vencimento [DATA]. Canal [CANAL]. Peça conferência se já tiver
sido pago. Não inclua dados bancários não fornecidos nem ofereça
acordo ou desconto. Não envie a mensagem.
```

**Saída esperada** — mensagem curta para revisão.

**Conferir** — saldo, identificação da obrigação e pagamento recente.

### 18. Procedimento administrativo

**Objetivo** — documentar uma rotina repetida.

**Entradas** — descrição atual, papéis e exceções.

```text
Use a skill A9 Educação. Documente a rotina [ROTINA] com base
em [DESCRIÇÃO]. Liste entrada, responsável, passos, resultado,
conferência e exceções conhecidas. Separe o procedimento atual das
melhorias propostas. Não crie regra de aprovação ou obrigação nova.
```

**Saída esperada** — procedimento claro e lista separada de melhorias.

**Conferir** — correspondência com o processo real.

## Pessoas e RH

### 19. Integração de equipe

**Objetivo** — orientar uma chegada ou mudança de rotina.

**Entradas** — função, atividades e orientações confirmadas.

```text
Use a skill A9 Educação. Prepare um guia de integração para
[FUNÇÃO], com atividades [LISTA] e orientações [REGRAS].
Organize primeiros passos, materiais e pessoas de referência quando
fornecidas. Não inclua dados pessoais, senhas, benefícios ou políticas
não confirmadas.
```

**Saída esperada** — guia de integração e pendências de informação.

**Conferir** — acessos, responsáveis e regras atuais.

### 20. Comunicação interna

**Objetivo** — tornar um comunicado compreensível.

**Entradas** — decisão aprovada, público e ação esperada.

```text
Use a skill A9 Educação. Redija um comunicado sobre [DECISÃO
APROVADA] para [PÚBLICO]. Informações [DADOS]. Explique o que
acontece, quando e qual ação a pessoa deve tomar. Preserve o sentido
da decisão e a privacidade. Não publique nem envie.
```

**Saída esperada** — comunicado pronto para revisar.

**Conferir** — decisão, prazo, público e próximo passo.

### 21. Perguntas frequentes

**Objetivo** — organizar orientações já existentes.

**Entradas** — documentos aprovados e dúvidas anonimizadas.

```text
Use a skill A9 Educação. Crie perguntas frequentes a partir de
[DOCUMENTOS APROVADOS] e [DÚVIDAS]. Cada resposta deve indicar sua
fonte e o que fazer se o caso não estiver coberto. Não invente
políticas, benefícios, obrigações ou decisões individuais.
```

**Saída esperada** — FAQ com fonte e encaminhamento.

**Conferir** — fidelidade às políticas atuais e dados pessoais removidos.

## Tecnologia e Produto

### 22. Briefing de ferramenta

**Objetivo** — esclarecer um problema antes de construir.

**Entradas** — problema, usuários, exemplos e restrições.

```text
Use a skill A9 Educação. Estruture um briefing para uma ferramenta
que apoie [PROCESSO]. Problema [RELATO]. Usuários [PERFIS].
Restrições [LISTA]. Defina objetivo, entrada, saída, fluxo principal
e critérios de aceite. Diferencie requisito confirmado de proposta.
Não invente integrações ou permissões.
```

**Saída esperada** — briefing implementável com lacunas identificadas.

**Conferir** — problema atendido e critérios observáveis.

### 23. Interface interna

**Objetivo** — construir uma tela com padrão A9.

**Entradas** — briefing e contrato dos dados.

```text
Use a skill A9 Educação para criar a interface de [TELA].
Briefing [REQUISITOS]. Dados e ações disponíveis [CONTRATO].
Aplique tokens A9, labels, validação, carregamento, vazio e erro.
Se houver lista grande, use busca e paginação adequadas. Não simule
persistência nem conecte o CRM sem solicitação.
```

**Saída esperada** — interface no formato e stack pedidos.

**Conferir** — teclado, responsividade, estados e ações reais.

### 24. Registro de problema

**Objetivo** — tornar uma falha reproduzível.

**Entradas** — relato, comportamento esperado e evidências sem segredos.

```text
Use a skill A9 Educação. Organize o problema [RELATO].
Esperado [COMPORTAMENTO]. Evidências autorizadas [EVIDÊNCIAS].
Entregue passos de reprodução, observado, esperado, impacto e
hipóteses a verificar. Separe hipótese de causa comprovada.
Remova credenciais e dados pessoais. Não altere produção.
```

**Saída esperada** — registro técnico claro.

**Conferir** — reprodução, impacto e evidências suficientes.

## Gestão e Liderança

### 25. Reunião de acompanhamento

**Objetivo** — transformar informações em pauta de decisão.

**Entradas** — dados do período e decisões pendentes.

```text
Use a skill A9 Educação. Prepare uma pauta de [DURAÇÃO] com
os dados [DADOS], do período [PERÍODO]. Mostre fatos, desvios,
perguntas de decisão e ações propostas. Cada ação deve ter responsável
e prazo sugeridos, identificados como proposta quando não aprovados.
Não invente metas ou decisões.
```

**Saída esperada** — pauta curta e quadro de decisões.

**Conferir** — origem dos números e distinção entre decisão e sugestão.

### 26. Comparação de alternativas

**Objetivo** — apoiar uma escolha com critérios claros.

**Entradas** — alternativas, critérios e evidências disponíveis.

```text
Use a skill A9 Educação. Compare [ALTERNATIVAS] para [OBJETIVO].
Critérios [CRITÉRIOS]. Evidências [DADOS]. Mostre vantagens,
limitações, custo confirmado e incertezas. Recomende uma opção com
justificativa. Não invente pontuações, preços ou capacidades.
```

**Saída esperada** — comparação rastreável e recomendação.

**Conferir** — critérios equivalentes e lacunas que alteram a escolha.

### 27. Plano de ação

**Objetivo** — organizar próximos passos executáveis.

**Entradas** — objetivo, restrições e recursos confirmados.

```text
Use a skill A9 Educação. Proponha um plano para [OBJETIVO],
considerando [RESTRIÇÕES] e [RECURSOS]. Organize ações, sequência,
responsáveis sugeridos, prazo sugerido e evidência de conclusão.
Priorize o que pode ser verificado. Não trate sugestões como decisões
aprovadas e não crie tarefas em sistemas sem solicitação.
```

**Saída esperada** — plano de ação com critério de conclusão.

**Conferir** — dependências, capacidade e aprovação dos responsáveis.
