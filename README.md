# Intent Classifier

Customer intent classifier for e-commerce using LLM (Llama 3.3 70B) via Groq API.

## What it does
Receives customer messages and automatically classifies the intent into categories:
- CANCELAMENTO (Cancellation)
- RASTREAMENTO (Tracking)
- TROCA_DEVOLUCAO (Exchange/Return)
- RECLAMACAO (Complaint)
- DUVIDA_PRODUTO (Product question)
- PAGAMENTO (Payment)
- OUTRO (Other)

## Stack
- Python
- Groq API
- Llama 3.3 70B

## How to run
```bash
pip install groq
export GROQ_API_KEY=your_key_here
python classificador.py
```
