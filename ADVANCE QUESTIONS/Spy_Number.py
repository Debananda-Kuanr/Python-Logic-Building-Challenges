# 22. Check Whether a Number is a Spy Number
# Example:
# 1124
# Sum = 8
# Product = 8
# Spy Number

Number= int(input("Enter a Number:"))
Sum=0
Product=1

while Number>0:
    Digit= Number%10
    Sum+=Digit
    Product*=Digit
    Number=Number//10
if Sum==Product:
    print("This is a Spy Number")
else:
    print("This is not a Spy Number")