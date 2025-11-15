n = int(input("Number of products purchased: "))
price = float(input("Product price: "))

if n <= 2:
    total = n * price
else:
    total = n * price * 0.75

print(f"Amount to pay: {total}")