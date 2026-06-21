# 8. Vending Machine
# Menu:
# 1. Chips ₹20
# 2. Biscuit ₹10
# 3. Cold Drink ₹40

# User inserts money.

# If enough:
# Product Delivered
# Balance Returned

# Else:
# Insufficient Amount

while 1:
    print("""
1. Chips ₹20
2. Biscuit ₹10
3. Cold Drink ₹40
4. Exit
""")

    choice = int(input("Enter Your Choice: "))

    match choice:
        case 1:
            item = "Chips"
            price = 20

        case 2:
            item = "Biscuit"
            price = 10

        case 3:
            item = "Cold Drink"
            price = 40

        case 4:
            print("Exiting...")
            break

        case _:
            print("Invalid Choice")
            print()
            continue

    print(item, f"₹{price}/per")

    qnt = int(input("Enter Quantity: "))

    if qnt <= 0:
        print("Invalid Quantity")
        print()
        continue

    total = price * qnt

    print("Total Amount:", total)

    ins_amt = int(input("Insert Amount: "))

    if ins_amt >= total:
        print("Product Delivered")
        print("Balance Returned:", ins_amt - total)
    else:
        print("Insufficient Amount")

    print()