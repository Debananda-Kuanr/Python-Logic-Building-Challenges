# 2. Bus Ticket Booking System

# A bus has 20 seats.

# User enters seat number.
# If seat already booked → show message.
# Otherwise book it.
# Show available seats option.

# Use loops and lists.

seats = [0]*20
print('''1. Book Seat
2. Show Available Seats
3. Exit''')

while 1:
    print()
    choice=int(input("Enter Your Choice: "))
    match choice:
        case 1:
            seat_no= int(input("Enter the Seat No. Want to Book (1-20): "))
            if seat_no < 1 or seat_no > 20:
                print("Invalid seat number!")
            else:
                if seats[seat_no-1] == 0:
                    print("Seat Booked Sucessful...")
                    seats[seat_no-1]=1
                else:
                    print("Seat is Already Booked")

        case 2:
            print("Seat Available:")
            for i in range(20):
                if seats[i]==0:
                    print(i+1,end=" ")
            print()
            print("Seat Booked:")
            for i in range(20):
                if seats[i]==1:
                    print(i+1,end=" ")
                

            print()
        
        case 3:
            break
        case _:
            print("Invalid Choice")