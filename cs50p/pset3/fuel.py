def main():

    while True:
        try:

            fraction = input("Fraction: ")

            x, y = fraction.split("/")

            x = int(x)
            y = int(y)

            percent = round(x / y * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if x <= y:
                break

    if percent <= 1:
        print("E")
    elif percent >= 99: 
        print("F")
    else:
        print(f"{percent}%")


main()