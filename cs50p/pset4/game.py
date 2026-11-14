import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        # só aceita inteiro positivo
        if level > 0:
            break

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else: 
        if guess < 1:
            pass
        elif guess < number: 
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else: 
            print("Just right!")
            break