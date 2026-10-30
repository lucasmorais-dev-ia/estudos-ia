saudacao = input("qual foi a sua saudacao? ").strip().lower()

if saudacao.startswith("hello"):
    print("$0")
elif saudacao.startswith("h"):
    print("$20")
else:
    print("$100")
    