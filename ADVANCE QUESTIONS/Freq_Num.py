# 23. Find Frequency of Every Digit
# Input:
# 122334455
# Output:
# 1 -> 1
# 2 -> 2
# 3 -> 2
# 4 -> 2
# 5 -> 2

Number = int(input("Enter a Number: "))
for digit in range(10):
    count = 0
    temp = Number

    while temp>0:
        last_digit=temp%10
        if last_digit==digit:
            count+=1
        temp=temp//10
    if count>0:
        print(f"{digit}->{count}")
