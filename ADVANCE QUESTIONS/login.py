# 14. Login System
# Correct credentials:
# Username: admin
# Password: python123

# User gets only 3 attempts.
# After 3 failures:
# Account Locked

Username= "admin"
Password= "python123"

attempt = 0

while attempt < 3:
    print()
    user = input("Username: ")
    password = input("Password: ")

    if user == Username and password == Password:
        print("Login Successful")
        break
    else:
        attempt += 1
        if attempt == 3:
            print("Account Locked")
        else:
            print("Invalid credentials. Attempts left:", 3 - attempt)