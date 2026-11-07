bar = ["caipirinha", "mojito", "gin_tonica"]

for i in range(len(bar)):
    print(i + 1, bar[i])


while True:
    dose = int(input("quantas doses? "))
    if dose > 0:
        break


for _ in range(dose):
    print("dose")