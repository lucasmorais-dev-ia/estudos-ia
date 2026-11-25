# anthropic = biblioteca oficial para conversar com a API do Claude
import anthropic

# client = cliente; ele procura a ANTHROPIC_API_KEY sozinho nas variáveis de ambiente
client = anthropic.Anthropic()

# messages.create = manda uma conversa para o modelo e espera a resposta
message = client.messages.create(
    # model = qual modelo responde (o Haiku é o mais barato)
    model="claude-haiku-5-5",
    # max_tokens = tamanho máximo da resposta
    max_tokens=200,
    # messages = a conversa: uma lista de dicionários, cada um com quem fala e o texto
    messages=[
        {"role": "user", "content": "quanto é 100-33 ?"},
    ],
)

# content[0].text = o texto da primeira parte da resposta
print(message.content[0].text)

