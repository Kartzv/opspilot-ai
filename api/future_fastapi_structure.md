# Estrutura Futura com FastAPI

Este documento descreve uma possivel estrutura futura da API.

## Rotas Futuras

```txt
GET /contacts
POST /contacts
GET /contacts/{id}
GET /contacts/search?phone=
POST /requests
GET /requests
PATCH /requests/{id}/status
POST /tasks
GET /tasks
PATCH /tasks/{id}/status
GET /reports/summary
```

## Possivel Organizacao Futura

```txt
api/
├── main.py
├── routes/
│   ├── contacts.py
│   ├── requests.py
│   ├── tasks.py
│   └── reports.py
├── schemas/
│   ├── contact_schema.py
│   ├── request_schema.py
│   └── task_schema.py
└── dependencies.py
```

## Observacao

FastAPI nao sera implementado agora. Primeiro vamos construir a base em Python puro.
