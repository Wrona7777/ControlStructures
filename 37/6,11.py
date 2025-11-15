previous_price = 200.00
current_price  = 140.00

print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")

reduction_pct = (previous_price - current_price) / previous_price * 100

if reduction_pct >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {reduction_pct}%")