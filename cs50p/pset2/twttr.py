def main(): 
    text = input("Input: ")
    output = convert(text)

    print("Output:", output)


def convert(text):
    result = ""
    for c in text:
        if c not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            result = result + c

    return result


main()

