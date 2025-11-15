time_24 = input("Podaj czas (format 24h): ")

hh_str = time_24[0:2]
mm_str = time_24[3:5]

hh = int(hh_str)
mm = int(mm_str)

if hh == 0:
    hh12 = 12
    suffix = "am"
elif hh < 12:
    hh12 = hh
    suffix = "am"
elif hh == 12:
    hh12 = 12
    suffix = "pm"
else:
    hh12 = hh - 12
    suffix = "pm"

print(f"Czas w formacie 12h: {hh12}:{mm_str}{suffix}")