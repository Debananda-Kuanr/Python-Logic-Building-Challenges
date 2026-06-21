# 3. Password Strength Checker

# User enters a password.

# Check:

# Length ≥ 8
# Contains digit
# Contains uppercase letter
# Contains lowercase letter

# Print:

# Weak
# Medium
# Strong

password= input("Enter Your Password: ")
Score=0

if len(password)>=8:
    Score+=1

for i in password:
    if i.isdigit():
        Score+=1
        break

for i in password:
    if i.isupper():
        Score+=1
        break

for i in password:
    if i.islower():
        Score+=1
        break

if Score<=2:
    print("Weak Password") 
elif Score ==3:
    print("Medium Password")
else:
    print("Strong Password")