name = input("Enter name: ")

if len(name) > 0 and name[-1] == "a":
    print(f"{name} -- Polish female name")
else:
    print("Prolly not a Polish female name")