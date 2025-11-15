amount = int(input("Enter the amount in PLN: "))

coins_5 = amount // 5
remainder = amount % 5

coins_2 = remainder // 2
remainder = remainder % 2

coins_1 = remainder

print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")