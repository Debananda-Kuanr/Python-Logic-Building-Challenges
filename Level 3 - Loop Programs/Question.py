#Print numbers from 1 to 100
# for i in range(1,101):
#     print(i)


#Print even numbers from 1 to 100.
# for i in range(1,101):
#     if i%2==0:
#         print(i,end=" ")


#Print odd numbers from 1 to 100.
# for i in range(1,101):
#     if i%2!=0:
#         print(i, end=" ")


#Find the sum of first N natural numbers
# N= int(input("Enter The Value of N: "))
# Sum=0
# for i in range(1,N+1):
#     Sum+=i
# print("The Sum of 1st",N,"Number is",Sum)


#Find the factorial of a number
# Num= int(input("Enter the Number For Factorial: "))
# Fact=1
# for i in range(1,Num+1):
#     Fact*=i
# print("The Factorial of",Num,"is",Fact)


#Print the multiplication table of a number
# Num= int(input("Enter a Number For the Multiplication Table: "))
# for i in range(1,11):
#     print(Num,"x",i,"=",Num*i)


#Count digits in a number
# Num=input("Enter a Number: ")
# Digit=0
# for i in Num:
#     Digit+=1
# print(Num,"is a",Digit,"digit Number")


#Reverse a number
# Num= int(input("Enter a Number: "))
# Reverse=0
# while Num>0:
#     digit=Num%10
#     Reverse=Reverse*10+digit
#     Num=Num//10
# print("The Reverse Number is:",Reverse)


#Check whether a number is a palindrome
# Num= int(input("Enter a Number: "))
# Temp=Num
# Reverse=0
# while Temp>0:
#     digit=Temp%10
#     Reverse=Reverse*10+digit
#     Temp=Temp//10
# if Num==Reverse:
#     print("This is a Palidrom Number")
# else:
#     print("This is not a Palidrom Number")


#Find the sum of digits of a number
# Num= int(input("Enter the Number For Sum Each Digit: "))
# sum=0
# while Num>0:
#     Digit=Num%10
#     sum+=Digit
#     Num=Num//10
# print("Sum is:",sum)


#Find the product of digits
# Num= int(input("Enter the Number For Multiply Each Digit: "))
# Multiplication=1
# while Num>0:
#     Digit=Num%10
#     Multiplication*=Digit
#     Num=Num//10
# print("Multiplication is:",Multiplication)


#Check whether a number is an Armstrong number
# Num=input("Enter a Number to Check Armstrong or not: ")
# temp= int(Num)
# Pow=len(Num)
# Sum=0
# while temp>0:
#     digit=temp%10
#     Sum=Sum+(digit**Pow)
#     temp=temp//10
# if int(Num)==Sum:
#     print("This is an Armstrong Number")
# else:
#     print("This is not an Armstrong Number")