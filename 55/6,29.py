numbers_amount = int(input("Podaj ile prime numberow chcesz "))

count = 0

current_prime_number = 2

while numbers_amount > count:
    is_prime = True
    divisor = 2

    while divisor * divisor <= current_prime_number:
        if current_prime_number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(current_prime_number, end=" ")
        count += 1
    current_prime_number += 1

print()






