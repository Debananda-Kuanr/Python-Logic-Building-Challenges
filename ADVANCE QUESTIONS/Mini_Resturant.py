# 20. Mini Restaurant Management System

# Menu:
# Burger  ₹80
# Pizza   ₹150
# Coffee  ₹40

# User can order multiple items.
# At end print:

# Ordered items
# Quantity
# Total Bill
# GST (5%)
# Final Amount

pizza,burger,coffee=0,0,0

print("""
------ Menu ------
1. Burger  ₹80
2. Pizza   ₹150
3. Coffee  ₹40
------------------
""")

while True:
    item= input("Enter item name (Burger/Pizza/Coffee) or Done:").lower()

    if item=="pizza":
        Qnt=int(input("Quantity:"))
        pizza+=Qnt
    elif item=="burger":
        Qnt=int(input("Quantity:"))
        burger+=Qnt   
    elif item=="coffee":
        Qnt=int(input("Quantity:"))
        coffee+=Qnt
    elif item=="done":
        print("Thankyou...")
        break   
    else:
        print("Invalid Item")

Total_Bill= burger*80 + pizza*150 + coffee*40
gst=Total_Bill*0.05
Final_Bill=Total_Bill+gst 

print()
print("--------- Bill ---------")
if pizza>0:
    print("Pizza: 150 x",pizza,"=",150*pizza)
if burger>0:
    print("Burger: 80 x",burger,"=",80*burger)
if coffee>0:
    print("Coffee: 40 x",coffee,"=",40*coffee)
print("------------------------")
print(f"""Total Amount: {Total_Bill}
GST(5%): {gst}
Final Amount: {Final_Bill}
------------------------
""")