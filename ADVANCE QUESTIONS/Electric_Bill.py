# 4. Smart Electricity Bill Generator
# Input units consumed.
# Rules:
# 0-100      ₹5/unit
# 101-300    ₹7/unit
# Above 300  ₹10/unit

# Calculate total bill.
# Add 18% GST

Bill= int(input("Enter Unit you Consumed: "))

if Bill <= 100:
    bill = Bill * 5

elif Bill <= 300:
    bill = (100 * 5) + ((Bill - 100) * 7)

else:
    bill = (100 * 5) + (200 * 7) + ((Bill - 300) * 10)

print("Bill Amount:",bill)
print("Tax Amount:",bill*0.18)
print("Total Bill Amount:",bill+(bill*0.18))
