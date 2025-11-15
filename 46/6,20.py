number = int(input("Enter decimal number: "))

original = number
if number == 0:
    binary = "0"
else:
    binary = ""
    while number > 0:
        r = number % 2
        binary = str(r) + binary
        number = number // 2

print(f"{original}(10) = {binary}(2)")