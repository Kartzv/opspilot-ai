# Arquitetura

O OpsPilot AI sera construido em camadas, mas sem comecar complexo demais.

Na primeira fase, a arquitetura sera propositalmente simples para facilitar o aprendizado de Python.

## Fase Inicial

```txt
Terminal
↓
Funcoes procedural
↓
Dados em memoria
```

Nesta etapa, o foco sera praticar:

- input e print;
- condicionais;
- loops;
- listas;
- dicionarios;
- sets;
- funcoes.

Os dados ainda poderao existir apenas enquanto o programa estiver rodando.

## Evolucao com JSON e Modulos

```txt
Terminal
↓
Funcoes procedural
↓
Arquivos JSON
```

Depois, o projeto passa a salvar dados em arquivos locais dentro da pasta `data`.

Isso permite aprender:

- leitura de arquivos;
- escrita de arquivos;
- JSON;
- tratamento de erros;
- organizacao de funcoes por modulo.

## Evolucao com Services e Repositories

```txt
Terminal
↓
Services
↓
Repositories
↓
JSON/PostgreSQL
```

Quando chegar a fase de Programacao Orientada a Objetos, as regras de negocio ficarao em `services` e o acesso aos dados ficara em `repositories`.

Essa separacao ajuda a entender responsabilidades:

- CLI conversa com o usuario;
- services aplicam regras;
- repositories salvam e carregam dados.

## Evolucao Futura com API

```txt
FastAPI
↓
Services
↓
Repositories
↓
PostgreSQL
```

Quando o projeto virar uma API, o terminal deixara de ser a interface principal. O FastAPI passara a receber requisicoes HTTP e chamar os services.

## Evolucao Futura com IA

```txt
FastAPI
↓
Services
↓
Repositories
↓
PostgreSQL
↓
IA/LangChain
```

A camada de IA sera adicionada apenas quando a base do backend estiver mais madura.

Ela podera ajudar a:

- classificar mensagens;
- extrair dados;
- gerar resumos;
- sugerir proximas acoes;
- consultar uma base de conhecimento;
- acionar tools internas.
