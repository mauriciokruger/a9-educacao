# Validação da versão 1.2.0

Realizada em 29/10/2026. O novo guia de plataformas foi comparado com a main atual do CRM e integrado à skill e ao pacote. Os seis testes de distribuição e dos recursos existentes passaram. Veja a [comparação e o alcance da validação](VALIDACAO-PLATAFORMAS.md).

## Histórico da versão 1.1.0

Realizada em 28/10/2026.

## E-mails e assinaturas

A versão anterior tinha orientações gerais de e-mail, mas não distribuía o modelo completo. Uma mensagem criada a partir dela ficou com um fechamento simples em lugar da assinatura configurada. Essa lacuna orientou a atualização.

O pacote agora inclui o guia E-mails e Assinaturas, o modelo de e-mail, o bloco de assinatura e uma imagem demonstrativa para o lugar da foto. São 26 arquivos na skill. Nenhuma foto, assinatura ou informação pessoal real faz parte do pacote público.

O teste do contrato dos modelos falhou antes da inclusão dos arquivos e passou depois. Ele verifica uma única assinatura por modelo, o espaço da foto, o texto alternativo e a resolução local das imagens.

Uma avaliação independente usou a skill atualizada em três pedidos com dados demonstrativos.

| Pedido | Resultado |
| --- | --- |
| E-mail com assinatura e foto já fornecidas | O bloco original foi preservado, uma única vez |
| E-mail sem assinatura ou foto disponíveis | O corpo foi preparado e os dados ausentes foram solicitados |
| E-mail com pedido explícito para retirar a assinatura | A versão foi criada sem a assinatura pessoal |

O modelo foi renderizado e inspecionado em uma janela larga e em uma janela de conteúdo de 390 px, com carregamento local da logo e da imagem de exemplo. Os seis testes do repositório passaram.

A assinatura com foto e os padrões de novas mensagens e respostas foram conferidos em uma conta Gmail. As configurações existentes foram preservadas. A mensagem de referência já tinha sido enviada e não foi alterada.

Os testes locais do modelo não comprovam entrega em todos os programas de e-mail. Uma assinatura fornecida por CID depende do anexo correspondente na mensagem real. A imagem de exemplo do pacote precisa ser substituída pela foto autorizada de quem vai enviar.

## Histórico da versão 1.0.1

Realizada em 27/10/2026.

## Teste prático após instalação

A skill foi reconhecida no catálogo desta sessão do Codex. Uma instalação limpa do GitHub também foi conferida com o instalador oficial do Codex, em pasta temporária, sem substituir a instalação pessoal durante o teste.

Usando exclusivamente as referências, fontes, logo e modelo da pasta instalada, foram criados dois materiais novos.

- [Apresentação de seis slides](exemplos/primeiro-pedido-a9.html), sobre como pedir materiais à IA, com [PDF de seis páginas](exemplos/primeiro-pedido-a9.pdf).
- [Landing page de oficina fictícia](exemplos/oficina-produtividade.html), com informações comerciais pendentes e links internos.

Os exemplos públicos não contêm dados de clientes. Os HTMLs incorporam as fontes, a logo e as licenças. Não dependem do repositório para abrir.

O teste identificou duas falhas no modelo instalado da versão 1.0.0, corrigidas nesta versão e nos novos exemplos.

1. O índice de slides ficava oculto no celular e os alvos eram pequenos. Agora permanece visível, com alvos de 40 × 44 px. A barra também reserva altura suficiente entre 761 e 1100 px, evitando corte parcial dos indicadores em tablets.
2. As setas navegavam entre slides dentro de alguns campos editáveis. O tratamento passou a respeitar `isContentEditable`, incluindo conteúdo editável herdado por elementos filhos.

Os testes de regressão falharam antes das correções e passaram depois. No Chrome isolado, com resolução externa de nomes bloqueada.

| Material | Verificações automáticas | Resultado |
| --- | --- | --- |
| Demonstração de oito slides | 51 verificações de fontes, cortes, índice, limites, teclado e movimento reduzido | Passou |
| Apresentação nova de seis slides | 43 verificações em desktop, tablet e celular | Passou |
| Landing page fictícia | 10 verificações de fontes, largura, texto, âncoras e ausência de cadastro e recursos externos | Passou |

Todas as seis páginas do novo PDF foram renderizadas e inspecionadas. A landing page foi inspecionada em desktop e em uma janela de conteúdo de 390 px. A nova capa do README foi renderizada com Poppins e a logo oficial.

Os textos do pacote e dos exemplos também foram revisados. A orientação de escrita agora pede linguagem próxima e clara, sem travessão, ponto e vírgula ou dois-pontos na redação. A pontuação de código, endereços, metadados e licenças originais foi preservada.

## Pacote

- Estrutura de uma única skill, metadados, referências locais e assets conferidos.
- ZIP com uma pasta raiz a9-educacao, sem arquivos de desenvolvimento ou credenciais.
- Fontes locais, licenças originais e três logos oficiais incluídas.
- CSS gerado a partir dos tokens JSON.
- 27 prompts em nove áreas de aplicação.
- Construção e testes do pacote executados localmente.

## Apresentações

- Oito tipos de slide no modelo e oito slides na demonstração.
- Poppins e JetBrains Mono carregadas no renderizador.
- Todos os slides verificados para cortes e rolagem horizontal em larguras de 1280 e 390 px.
- Navegação por índice, seta, Home e End e limites inicial/final verificados.
- Atalhos preservam a digitação em inputs e a ativação de botões por espaço.
- Movimento reduzido e ausência de dependências externas verificados.
- PDF gerado pelo CSS de impressão do próprio HTML em Chrome isolado, com oito páginas 16 por 9.
- Todas as páginas do PDF renderizadas e inspecionadas visualmente.
- Inspeção na sessão interativa confirmou a capa e um slide de conteúdo. A impressão pela janela interativa foi interrompida pela ferramenta de controle. A exportação foi concluída pelo renderizador local isolado.
- O botão de tela cheia e seu tratamento de indisponibilidade estão incluídos. Não foi realizado teste manual de tela cheia nos diferentes navegadores.

## Comportamento da skill

Avaliação independente comparou os mesmos tipos de pedido antes e depois do guia.

| Cenário | Sem o guia | Com o guia |
| --- | --- | --- |
| Apresentação A9 sem formato | PowerPoint e identidade provisória | HTML, fontes, paleta e estrutura A9 |
| Landing page fictícia | Identidade provisória | Identidade A9 e condições ausentes identificadas |
| Proposta sem valores | Minuta com lacunas | Composição A9 e separação entre confirmado e sugerido |
| Explicação de geometria | Explicação comum | Explicação comum, sem impor a marca A9 |

Esses testes avaliam recuperação e aplicação das regras, sem garantir que toda resposta futura de um modelo será idêntica.

## Instalação

A pasta da skill foi instalada e conferida por comparação de todos os arquivos em uma localização de skills pessoais do Codex neste computador. A versão 1.0.1 substitui a cópia anterior nessa mesma pasta. Não foi criada uma segunda instalação concorrente.

Upload nativo e habilitação no ChatGPT, Claude web e Claude Code não foram testados nesta versão. As instruções foram conferidas com a documentação oficial disponível na data. Disponibilidade, permissões e menus podem variar por conta ou workspace.

## Reproduzir verificações

Python 3.10 ou superior.

```sh
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

Para verificar o HTML em um Chrome instalado, sem perfil ou credenciais pessoais.

```sh
python scripts/check_local.py --chrome "CAMINHO_DO_CHROME"
python scripts/check_local.py --chrome "CAMINHO_DO_CHROME" --mode pdf
```

Para conferir o exemplo novo de seis slides.

```sh
python scripts/check_local.py --chrome "CAMINHO_DO_CHROME" --deck docs/exemplos/primeiro-pedido-a9.html --expected-slides 6
python scripts/check_local.py --chrome "CAMINHO_DO_CHROME" --mode pdf --deck docs/exemplos/primeiro-pedido-a9.html --expected-slides 6 --pdf-output docs/exemplos/primeiro-pedido-a9.pdf
```

O teste local usa apenas um servidor temporário em 127.0.0.1 e um perfil isolado em .work. Os relatórios locais não entram no ZIP.

Os testes opcionais do PDF usam pypdf, Pillow e PNGs produzidos pelo Poppler. Sem essas bibliotecas, a verificação do pacote continua disponível e os testes opcionais são sinalizados como não executados.
