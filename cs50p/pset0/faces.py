def main():
    print(convert(input("type something ")))



def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()