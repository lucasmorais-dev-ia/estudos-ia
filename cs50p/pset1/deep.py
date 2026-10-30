name = input("qual a resposta para a grande pergunta do universo e tudo mais? ").lower()

match name:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")