# 13. Library Fine Calculator
# Input:
# Book issue days
# Allowed days = 15

# Fine:
# 1-5 days late      ₹2/day
# 6-10 days late     ₹5/day
# Above 10 days      ₹10/day
# Calculate total fine.

Book_Issue= int(input("Enter the Book Issue Days: "))

if Book_Issue<=15:
    print("Fine Amount: 0")
else:
    extra_day=Book_Issue-15
    if 1<=extra_day<=5:
        print("Fine Amount:",extra_day*2)
    elif 6<=extra_day<=10:
        print("Fine Amount:",extra_day*5)
    else:
        print("Fine Amount:",extra_day*10)