# 11. Parking Lot System

# Parking has 10 slots.

# Options:
# Park Vehicle
# Remove Vehicle
# View Slots
# Exit

# Keep updating slot status.

Slots=[0]*10
while 1:
    print()
    print("""1. Park Vehicle
2. Remove Vehicle
3. View Slots
4. Exit""")

    print()
    choice= int(input("Enter Your Choice:"))


    match choice:
        case 1 : 
            park=int(input("Enter the Slot you want to Parking:  "))
            if park<1 or park>10:
                print("Invalid Slot")
            else:
                if Slots[park-1]==1:
                    print("Already Occupied")
                else:
                    print("Vehicle parked at Slot",park)
                    Slots[park-1]=1
        case 2:
            Rem_park=int(input("Enter the Slot you want to Remove Vehicle:  "))
            if Rem_park<1 or Rem_park>10:
                print("Invalid Slot")
            else:
                if Slots[Rem_park-1]==1:
                    print(f"Vehicle Removed from Slot {Rem_park}")
                    Slots[Rem_park-1]=0
                else:
                    print("No Vehicle is there in slot ",Rem_park)
        case 3: 
            if 0 in Slots:
                    print("Slot Available:",end=" ")
                    for i in range(10):
                        if Slots[i]==0:
                            print(i+1,end=" ")
                    print()
                    print("Slot Occupied:",end=" ")
                    for i in range(10):
                        if Slots[i]==1:
                            print(i+1,end=" ")
            else:
                print("No Slots are available")
                print("Parking is Full")
                print()
        case 4:
            print("Thankyou")
            break
        case _:
            print("Invalid Choice")
            print()
                    