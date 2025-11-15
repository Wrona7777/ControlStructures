q1 = input("SURVEY Are you interested in computer science? (y/n): ")
q2 = input("Do you like playing computer games? (y/n): ")
q3 = input("Do you have an Instagram account? (y/n): ")

interested_cs = (q1 == 'y')
like_games = (q2 == 'y')
has_instagram = (q3 == 'y')

print("\nSURVEY RESULTS")
if interested_cs:
    print("Interested in computer science: Yes")
else:
    print("Interested in computer science: No")

if like_games:
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")

if has_instagram:
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")