# 16. Shopping Cart Program
# User enters item prices continuously.
# Stop when user enters 0.
# Calculate:
# Total
# Discount

# Rules:
# Above 5000 → 10%
# Above 10000 → 20%

# Generate final bill.

Total_Price=0
Discount=0
while True:
    Price= int(input("Enter Item Price:"))

    if Price==0:
        break
    Total_Price+=Price

if Total_Price>=5000 and Total_Price<=9999:
    Discount=round(Total_Price*0.10,2)
elif Total_Price>=10000:
    Discount=round(Total_Price*0.20,2)
else:
    Discount=0

print(f"""
-------- BILL ---------
Total Amount: {Total_Price}
Discount: {Discount}
Final Amount: {Total_Price-Discount}
-----------------------
""")