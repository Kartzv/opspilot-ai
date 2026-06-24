# Estrutura Futura com LangChain

Este documento descreve o plano futuro para IA no OpsPilot AI.

## Funcionalidades Futuras

- classificar mensagem;
- extrair dados estruturados;
- gerar resumo;
- sugerir proxima acao;
- consultar base de conhecimento;
- criar tools para agentes;
- registrar analise no sistema.

## Exemplo de Analise Futura

```json
{
  "category": "commercial_request",
  "urgency": "high",
  "summary": "Cliente solicitou orcamento com entrega urgente.",
  "next_action": "Encaminhar para equipe comercial."
}
```

## Possivel Organizacao Futura

```txt
ai/
├── chains/
│   └── message_classifier.py
├── prompts/
│   └── classification_prompt.md
├── tools/
│   ├── contact_tools.py
│   └── task_tools.py
└── rag/
    ├── knowledge_base.md
    └── retriever.py
```

## Observacao

LangChain, RAG e LangGraph serao estudados depois que o backend estiver mais maduro.
