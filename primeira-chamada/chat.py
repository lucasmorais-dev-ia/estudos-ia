# 1. criar uma lista vazia para guardar memória.
# 2. repetir para sempre:
#     3. pedir texto para a pessoa.
#     4. se a pessoa digitou a palavra sair: parar o programa.
#     5. colocar a mensagem da pessoa na lista, com o papel "user"
#     6. mandar lista para a API.
#     7. mostrar na tela a mensagem do Claude
#     8. colocar a resposta do Claude na lista, com o papel "assistant"

import anthropic

client = anthropic.Anthropic()

# 1
messages = []

# 2
while True: 
    # 3
    text = input("Você: ")
    # 4
    if text == "sair":
        break
    # 5
    messages.append({"role": "user", "content": text})
    # 6
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=500,
        messages=messages,
    )
    # reply = resposta; começa vazia
    reply = ""
    # block = bloco; cada parte da resposta
    for block in response.content:
        # type = tipo; só o bloco de texto interessa
        if block.type == "text":
            reply = block.text
    # 7
    print(f"Claude: {reply}")
    # 8
    messages.append({ "role": "assistant", "content": reply})