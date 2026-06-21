# 9. Mobile Recharge System

# Plans:
# 1. ₹199
# 2. ₹299
# 3. ₹499

# Validate recharge amount.
# Generate receipt.
# Use match-case.

print("""Plans Available :
1. ₹199
2. ₹299
3. ₹499""")
price= int(input("Enter the Recharge Amount:"))
print()

match price:
    case 199:
        plan="199"
    case 299:
        plan="299"
    case 499:
        plan="499"
    case _:
        plan=None


if plan:
    print("Recharge Sucessful")
    print("Selected Plan:",plan)
    print(f"""
------RECIPT------
Recharge Amount: {plan}
Status: Active
""")
else:
    print("Invalid recharge amount!")
