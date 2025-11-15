hours = int(input("Podaj liczbę godzin parkowania: "))

if 1 <= hours <= 2:
    fee = 5
elif 3 <= hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
else:
    fee = 0  # za 0 godzin nic nie płacisz

print(f"Opłata: {fee} PLN")
