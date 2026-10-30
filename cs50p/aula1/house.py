name = input("what's you name? ")

match name:
    case "lucas" | "luanna" | "maria":
        print("lulahouse")
    case "vitor":
        print("flaviohouse")
    case _:
        print("who?")
