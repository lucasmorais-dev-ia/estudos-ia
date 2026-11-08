def main():
    print_square(3)


def print_square(size):

# para cada linha no quadrado
    for i in range(size):

# para cara tijolo na linha
        for j in range(size):

# print tijolo
            print("#", end="")

        print()


main()