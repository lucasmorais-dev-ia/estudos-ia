import random


def main():
    level = get_level()
    score = 0

    for problem in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        solved = False

        for attempt in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
            else:
                if answer == x + y:
                    score = score + 1
                    solved = True
                    break
                else:
                    print("EEE")

        if not solved:
            print(f"{x} + {y} = {x + y}")

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else: 
        return random.randint(100, 999)


if __name__ == "__main__":
    main()