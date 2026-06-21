# 6. Student Result Management

# Input marks of 5 subjects.

# Calculate:
# Total
# Percentage
# Grade

# Rules:
# 90+ A
# 80+ B
# 70+ C
# 60+ D
# Else F

# If any subject < 35 → Fail

marks=[0]*5
Tot_Mark=500
secu_mark=0
for i in range(5):
    while True:
        print("Enter the mark of Sub", i + 1, ":", end="")
        marks[i] = int(input())

        if 1 <= marks[i] <= 100:
            break
        else:
            print("Mark must be between 1 and 100. Please enter again.")
            print()

point=0
for i in range(5):
    if marks[i]>=35:
        point+=1

if point==5:
    for i in range(5):
        secu_mark+=marks[i]
    print("Total Secured mark:",secu_mark)
    percentage=round((secu_mark / Tot_Mark) * 100, 2)
    print("Total Percantege:",percentage)

    if percentage>=90:
        print("Your Grade : A")
    elif percentage>=80:
        print("Your Grade : B")
    elif percentage>=70:
        print("Your Grade : C")
    elif percentage>=60:
        print("Your Grade : D")
    else:
        print("Your Grade : F")

else:
    print("Your Grade : F")
