import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def classificar_intencao(mensagem):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """Você é um classificador de intenções de clientes para um e-commerce.
Classifique a mensagem do cliente em UMA das categorias abaixo e responda APENAS com a categoria e uma breve justificativa.

Categorias:
- CANCELAMENTO: cliente quer cancelar pedido
- RASTREAMENTO: cliente quer saber onde está o pedido
- TROCA_DEVOLUCAO: cliente quer trocar ou devolver produto
- RECLAMACAO: cliente está insatisfeito com produto ou serviço
- DUVIDA_PRODUTO: cliente tem dúvida sobre produto
- PAGAMENTO: cliente tem dúvida ou problema com pagamento
- OUTRO: não se encaixa nas categorias acima

Formato da resposta:
Categoria: <CATEGORIA>
Justificativa: <explicação curta>"""
            },
            {
                "role": "user",
                "content": mensagem
            }
        ]
    )
    return response.choices[0].message.content

# Testando
mensagens = [
    "Quero cancelar meu pedido, mudei de ideia",
    "Cadê meu pacote? Já faz 10 dias",
    "O produto chegou com defeito, quero devolver",
    "Vocês aceitam parcelamento em 12x?",
    "Esse tênis vem em tamanho 43?"
]

for msg in mensagens:
    print(f"\nMensagem: {msg}")
    print(classificar_intencao(msg))
    print("-" * 50)