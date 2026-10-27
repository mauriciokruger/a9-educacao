# Validação da versão 1.0.0

Realizada em 27/10/2026.

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
- Atalhos preservam a digitação em inputs.
- Movimento reduzido e ausência de dependências externas verificados.
- PDF gerado pelo CSS de impressão do próprio HTML em Chrome isolado, com oito páginas 16:9.
- Todas as páginas do PDF renderizadas e inspecionadas visualmente.
- Inspeção na sessão interativa confirmou a capa e um slide de conteúdo. A impressão pela janela interativa foi interrompida pela ferramenta de controle; a exportação foi concluída pelo renderizador local isolado.
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

A pasta da skill foi instalada e conferida por comparação de todos os arquivos em uma localização de skills pessoais do Codex neste computador.

Upload nativo e habilitação no ChatGPT, Claude web e Claude Code não foram testados nesta versão. As instruções foram conferidas com a documentação oficial disponível na data. Disponibilidade, permissões e menus podem variar por conta ou workspace.

## Reproduzir verificações

Python 3.10 ou superior:

```sh
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

Para verificar o HTML em um Chrome instalado, sem perfil ou credenciais pessoais:

```sh
python scripts/check_local.py --chrome "CAMINHO_DO_CHROME"
python scripts/check_local.py --chrome "CAMINHO_DO_CHROME" --mode pdf
```

O teste local usa apenas um servidor temporário em 127.0.0.1 e um perfil isolado em .work. Os relatórios locais não entram no ZIP.

Os testes opcionais do PDF usam pypdf, Pillow e PNGs produzidos pelo Poppler. Sem essas bibliotecas, a verificação do pacote continua disponível e os testes opcionais são sinalizados como não executados.
