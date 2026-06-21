# 15. Bank Interest Calculator

# Input:
# Principal
# Time
# Account Type
# Savings → 4%
# Current → 2%
# Fixed Deposit → 7%

# Calculate Simple Interest.
# Use match-case.
Intrest=0
Principal=int(input("Enter the Principal Amount: "))
Time=int(input("Enter the Time (in Year): "))
while True:
    print("""
Account Type (Rate Amount)
1. Saving -> 4%
2. Current -> 2%
3. Fixed Deposite ->7%
""")
    Acc_Typ=int(input("Enter Account Type(1-3): "))
    match Acc_Typ:
        case 1:
            Intrest=Principal*Time*0.04
            break
        case 2:
            Intrest=Principal*Time*0.02
            break
        case 3:
            Intrest=Principal*Time*0.07
            break
        case _:
            print("Invalid Choice ")

Total_Amount = Principal + Intrest
print("Interest:", Intrest)
print("Final Amount:", Total_Amount)