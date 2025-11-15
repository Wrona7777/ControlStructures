balance = 0.0
pin = "1234"  # startowy PIN

def deposit(bal):
    amt = float(input("Kwota wpłaty: "))
    return bal + amt

def withdraw(bal):
    amt = float(input("Kwota wypłaty: "))
    if amt <= bal:
        return bal - amt
    print("Za mało środków.")
    return bal

def show_balance(bal):
    print(f"Saldo: {bal}")
    return bal

# --- NOWE FUNKCJE ---

def check_pin(stored_pin):
    entered = input("Podaj PIN (4 cyfry): ")
    if len(entered) == 4 and entered.isdigit() and entered == stored_pin:
        print("PIN poprawny")
        return True
    print("PIN błędny")
    return False

def change_pin(stored_pin):
    current = input("Obecny PIN: ")
    if current != stored_pin:
        print("Błędny obecny PIN")
        return stored_pin
    new_pin = input("Nowy PIN (4 cyfry): ")
    if len(new_pin) == 4 and new_pin.isdigit():
        confirm = input("Potwierdź nowy PIN: ")
        if confirm == new_pin:
            print("PIN zmieniony")
            return new_pin
    print("Nie zmieniono PIN-u")
    return stored_pin

# --- proste menu do testu ---

while True:
    print("\n1) Wpłata  2) Wypłata  3) Saldo  4) Check PIN  5) Change PIN  0) Wyjście")
    choice = input("Wybór: ")

    if choice == "1":
        balance = deposit(balance)
    elif choice == "2":
        balance = withdraw(balance)
    elif choice == "3":
        show_balance(balance)
    elif choice == "4":
        check_pin(pin)
    elif choice == "5":
        pin = change_pin(pin)
    elif choice == "0":
        break
    else:
        print("Nieznana opcja")