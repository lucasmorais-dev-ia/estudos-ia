import inflect
joiner = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

print("Adieu, adieu, to " + joiner.join(names))