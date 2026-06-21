# Write a program to create a simple calculator using match-case
print('''1. Addition
2. Substraction
3. Multiplication
4. Division
5. Exit''')

while 1:
    print()
    Choice = int(input("Enter Your Choice: "))
    print()
    match Choice:
        case 1:
            print("Addition Operation")
            Num1=int(input("Enter 1st Number: "))
            Num2=int(input("Enter 2nd Number: "))
            print("Sum of ",Num1,"and",Num2,"is",Num1+Num2)
        case 2:
            print("Substraction Operation")
            Num1=int(input("Enter 1st Number: "))
            Num2=int(input("Enter 2nd Number: "))
            print("Subtraction of ",Num1,"and",Num2,"is",Num1-Num2)
        case 3:
            print("Multiplication Operation")
            Num1=int(input("Enter 1st Number: "))
            Num2=int(input("Enter 2nd Number: "))
            print("Multiplication of ",Num1,"and",Num2,"is",Num1*Num2)
        case 4:
            print("Division Operation")
            Num1=int(input("Enter 1st Number: "))
            Num2=int(input("Enter 2nd Number: "))
            print("Multiplication of ",Num1,"and",Num2,"is",Num1/Num2)
        case 5:
            break
        case _ :
            print("Opps!! Invalid Choice")