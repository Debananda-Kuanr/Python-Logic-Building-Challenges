# 5. Number Guessing Game

# Computer chooses a secret number (hardcode).

# User gets 5 chances.

# Show:
# Too High
# Too Low
# Correct

# Stop when guessed

import random
Com_Num = random.randint(1, 100)
Chance=5

for i in range(Chance):
    User_Num=int(input("Enter Your Number: "))

    if User_Num==Com_Num:
        print("Correct Number")
        break
    elif User_Num>Com_Num:
        print("Too High")
        print("Remaining Chances:", Chance - i - 1)
        print()
    else:
        print("Too Less")
        print("Remaining Chances:", Chance - i - 1)
        print()
else:
    print("Game Over! The secret number was", Com_Num)
    