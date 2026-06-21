# 18. Pattern Logic Challenge

# Input:
# n = 5
# Output:
# 1
# 12
# 123
# 1234
# 12345
# 4321
# 321
# 21
# 1
# No hardcoding.

n=int(input("Enter a Number:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()