# IA

A parte de IA sera adicionada somente depois que a base do projeto estiver bem estruturada.

## Objetivo Futuro

Usar IA generativa para entender mensagens operacionais e transformar texto livre em dados estruturados.

## Funcionalidades Futuras

- classificar tipo de solicitacao;
- identificar urgencia;
- extrair dados importantes;
- resumir conversas;
- sugerir proximas acoes;
- gerar resposta inicial;
- consultar base de conhecimento;
- registrar analises no sistema.

## Exemplo Futuro

Mensagem:

```txt
Bom dia, preciso de orcamento para concreto FCK 25, 8 metros, entrega amanha em Jacarepagua.
```

Analise esperada:

```json
{
  "tipo": "orcamento",
  "categoria": "concreto",
  "urgencia": "alta",
  "dados_extraidos": {
    "fck": "25",
    "volume_m3": 8,
    "local": "Jacarepagua",
    "data_entrega": "amanha"
  },
  "proxima_acao": "encaminhar para o comercial"
}
```

## Observacao

LangChain, RAG e LangGraph nao serao implementados agora. Eles fazem parte da evolucao futura do projeto.
