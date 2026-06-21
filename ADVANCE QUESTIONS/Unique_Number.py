# 19. Unique Number Analyzer
# Input a number.
#
# Find:
# Sum of digits
# Product of digits
# Largest digit
# Smallest digit
# Number of even digits
# Number of odd digits

# Do everything in one program.

num = int(input("Enter a number: "))

sum_digits = 0
product_digits = 1
largest = 0
smallest = 9
even_count = 0
odd_count = 0

temp = num

while temp > 0:
    digit = temp % 10


    sum_digits += digit


    product_digits *= digit

   
    if digit > largest:
        largest = digit


    if digit < smallest:
        smallest = digit


    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    temp = temp // 10

print()
print("Sum of digits =", sum_digits)
print("Product of digits =", product_digits)
print("Largest digit =", largest)
print("Smallest digit =", smallest)
print("Number of even digits =", even_count)
print("Number of odd digits =", odd_count)