# 17. Hotel Room Booking
# Rooms:
# Single
# Double
# Deluxe

# Each room has limited quantity.
# Book rooms until sold out.
# Show remaining rooms.

single=4
double=4
deluxe=4

while True:
    print("\nAvailable Rooms:")
    print("Single :", single)
    print("Double :", double)
    print("Deluxe :", deluxe)

    if single==0 and double==0 and deluxe==0:
        print("All Rooms are Sold Out")
        break
        
    room = input("Enter room type (Single/Double/Deluxe) or Exit: ").lower()

    if room == "exit":
        break
    if room == "single":
        if single > 0:
            single -= 1
            print("Single room booked successfully.")
        else:
            print("Single rooms are sold out.")

    elif room == "double":
        if double > 0:
            double -= 1
            print("Double room booked successfully.")
        else:
            print("Double rooms are sold out.")

    elif room == "deluxe":
        if deluxe > 0:
            deluxe -= 1
            print("Deluxe rooms booked successfully.")
        else:
            print("Deluxe rooms are sold out.")

    else:
        print("Invalid room type.")

