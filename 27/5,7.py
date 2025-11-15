number = int(input("Podaj numer, aby odliczyć go do zera: "))

for i in range(number, -1, -1):
    if i <= 5:
        if i == 5:
            print("Pięć")
        elif i == 4:
            print("Cztery")
        elif i == 3:
            print("Trzy")
        elif i == 2:
            print("Dwa")
        elif i == 1:
            print("Jeden")
        else:
            print(i)
    else:
        print(i)