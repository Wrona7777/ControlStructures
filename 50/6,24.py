number = 0

for i in range(1, 10):
    print("*", end="")
    if number > 0:
        for _ in range(number):
            print(" *", end="")
    print()

    if i < 5:
        number += 1
    else:
        number -= 1