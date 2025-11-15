age = int(input("Enter your age: "))

if age < 13:
    group = "Child"
elif 13 <= age <= 19:
    group = "Teen"
elif 20 <= age <= 64:
    group = "Adult"
else:
    group = "Senior"

print(f"You are in the '{group}' group.")