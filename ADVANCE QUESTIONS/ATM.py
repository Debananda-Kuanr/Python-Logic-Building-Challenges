# ATM Machine Simulation

# Create a program that shows:

# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Initial balance = ₹5000
# User can perform multiple operations.
# Withdrawal should fail if balance is insufficient.
# Exit only when user chooses Exit.

Current_Balance = 5000
print('''1. Check Balance
2. Deposit
3. Withdraw
4. Exit''')

while 1:
    Choice=int(input("Enter Your Choice: "))

    match Choice:
        case 1:
            print("Your Current balance is",Current_Balance)
            print()
        case 2:
            amt_to_dep= int(input("Enter the Amount Deposite:"))
            Current_Balance+=amt_to_dep
            print("Now Your Current balance is",Current_Balance)
            print()
        case 3:
            amt_to_wit = int(input("Enter the Amount For Withdraw: "))
            if amt_to_wit <= Current_Balance:
                Current_Balance -= amt_to_wit
                print("Now Your Current balance is", Current_Balance)
            else:
                 print("Insufficient Balance")
            print()
        case 4:
            break
        case _:
            print("Invalid Choice")
            print()