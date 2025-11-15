first_term = 0
second_term = 1

for index in range(20):
    print(first_term, end=" ")
    next_term = first_term + second_term
    first_term = second_term
    second_term = next_term
print()