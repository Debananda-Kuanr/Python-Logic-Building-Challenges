# 7. Digital Clock Simulation
# Input seconds.

# Convert into:
# Hours
# Minutes
# Seconds

# Example:
# 3665
# 1 Hour 1 Minute 5 Seconds

User_sec = int(input("Enter The Seconds: "))

hour = User_sec // 3600
User_sec %= 3600

minutes = User_sec // 60
User_sec %= 60

print(hour, "Hour", minutes, "Minute", User_sec, "Seconds")