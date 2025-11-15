dog_years = float(input("Podaj wiek psa w ludzkich latach: "))

first_years_increment = 10.5
standard_increment = 4

if dog_years <= 2:
    dog_years_calculated = dog_years * first_years_increment
else:
    dog_years_calculated = 2 * first_years_increment
    dog_years -= 2
    dog_years_calculated += standard_increment * dog_years

print(f"pies ma {dog_years_calculated} psich lat")