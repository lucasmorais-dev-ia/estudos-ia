def main():
    # 1. pedir o nome em camelCase
    camel = input("camelCase: ")
    # 2. converter (snake = cobra, o formato com _)
    snake = convert(camel)
    # 3. mostrar
    print("snake_case:", snake)


def convert(text):
    # result = resultado; começa como texto vazio
    result = ""
    # para cada letra (c) do texto
    for c in text:
        # isupper() = "é maiúscula?"
        if c.isupper():
            # junta um _ e a letra em minúscula
            result = result + "_" + c.lower()
        else:
            # junta a letra como está
            result = result + c
    return result


main()