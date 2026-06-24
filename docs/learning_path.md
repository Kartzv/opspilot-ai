# Learning Path

Este documento mostra o que sera aprendido em cada fase do OpsPilot AI.

## Fase 1 - Python basico

Nesta fase, o objetivo e criar uma aplicacao simples no terminal, sem classes e sem frameworks.

Conceitos praticados:

- variaveis;
- strings;
- numeros;
- input;
- print;
- if, elif e else;
- while;
- for;
- listas;
- dicionarios;
- sets;
- append;
- get;
- add;
- funcoes;
- return;
- try/except basico.

Objetivo pratico: cadastrar contatos, solicitacoes e tarefas usando estruturas simples do Python.

## Fase 2 - JSON

Nesta fase, o sistema passa a salvar dados em arquivos locais.

Conceitos praticados:

- open;
- with;
- json.load;
- json.dump;
- FileNotFoundError;
- tratamento de erros;
- persistencia simples.

Objetivo pratico: carregar os dados ao iniciar o programa e salvar alteracoes ao sair.

## Fase 3 - Modulos

Nesta fase, o projeto sera dividido em arquivos menores.

Conceitos praticados:

- import;
- modulos proprios;
- separacao de responsabilidades;
- organizacao de projeto.

Objetivo pratico: separar menu, funcoes de contato, funcoes de solicitacao, funcoes de tarefa, validacoes e relatorios.

## Fase 4 - Programacao Orientada a Objetos

Nesta fase, parte do projeto sera reescrita usando classes.

Conceitos praticados:

- class;
- __init__;
- self;
- atributos;
- metodos;
- encapsulamento simples;
- services;
- repositories.

Objetivo pratico: criar modelos e servicos para organizar melhor as regras de negocio.

## Fase 5 - Testes

Nesta fase, o projeto ganha testes automatizados.

Conceitos praticados:

- pytest;
- funcoes de teste;
- asserts;
- testes de regras de negocio;
- testes de casos de erro.

Objetivo pratico: garantir que funcoes importantes continuem funcionando conforme o projeto cresce.

## Fase 6 - PostgreSQL

Nesta fase, os arquivos JSON serao substituidos por banco de dados relacional.

Conceitos praticados:

- SQL;
- CREATE TABLE;
- INSERT;
- SELECT;
- UPDATE;
- DELETE;
- relacionamentos;
- conexao Python + PostgreSQL.

Objetivo pratico: armazenar contatos, solicitacoes, tarefas, analises de IA e eventos em tabelas.

## Fase 7 - FastAPI

Nesta fase, o sistema vira uma API REST.

Conceitos praticados:

- HTTP;
- GET;
- POST;
- PATCH;
- rotas;
- schemas;
- validacao;
- status codes.

Objetivo pratico: permitir que outros sistemas consumam o OpsPilot AI.

## Fase 8 - IA com LangChain

Nesta fase, a IA sera usada para interpretar mensagens operacionais.

Conceitos praticados:

- prompts;
- modelos de linguagem;
- saida estruturada;
- classificacao;
- extracao de dados;
- resumo;
- sugestao de proxima acao.

Objetivo pratico: transformar mensagens livres em dados uteis para a operacao.

## Fase 9 - RAG

Nesta fase, a IA passa a consultar uma base de conhecimento.

Conceitos praticados:

- documentos;
- embeddings;
- busca semantica;
- recuperacao de contexto;
- respostas com base em conhecimento interno.

Objetivo pratico: responder usando regras, servicos, politicas e informacoes da empresa.

## Fase 10 - LangGraph

Nesta fase, o projeto podera evoluir para agentes com estado e ferramentas.

Conceitos praticados:

- agentes;
- estado;
- tools;
- fluxos;
- tomada de decisao em etapas.

Objetivo pratico: permitir que a IA consulte dados, crie tarefas, atualize solicitacoes e registre eventos.
