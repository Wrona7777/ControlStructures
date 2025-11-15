correct_pin = "0805"

for _ in range(3):
    entered = input("Enter the PIN code: ")
    if entered == correct_pin:
        print("Correct!")
        break
    else:
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")