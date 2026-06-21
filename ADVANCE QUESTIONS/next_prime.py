# 21. Find the Next Prime Number after N
# Example:
# Input: 20
# Output: 23


n = int(input("Enter a number: "))

num = n + 1

while True:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print("Next Prime Number:", num)
        break
    num += 1