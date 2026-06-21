# 24. Mini Quiz Application
# 5 questions
# Multiple choice
# Score calculation
# Final result
# Pass/Fail

score = 0
print("========== QUIZ ==========")
print()
print("1. Which shortcut is used to Copy?")
print("a) Ctrl + X")
print("b) Ctrl + C")
print("c) Ctrl + V")
ans = input("Enter your answer: ")

if ans.lower() == "b":
    score += 1

print()
print("2. Which shortcut is used to Paste?")
print("a) Ctrl + V")
print("b) Ctrl + C")
print("c) Ctrl + Z")
ans = input("Enter your answer: ")

if ans.lower() == "a":
    score += 1

print()
print("3. Which shortcut is used to Cut?")
print("a) Ctrl + C")
print("b) Ctrl + X")
print("c) Ctrl + S")
ans = input("Enter your answer: ")

if ans.lower() == "b":
    score += 1

print()
print("4. Which shortcut is used to Undo?")
print("a) Ctrl + Y")
print("b) Ctrl + U")
print("c) Ctrl + Z")
ans = input("Enter your answer: ")

if ans.lower() == "c":
    score += 1

print()
print("5. Which shortcut is used to Save a file?")
print("a) Ctrl + S")
print("b) Ctrl + P")
print("c) Ctrl + A")
ans = input("Enter your answer: ")

if ans.lower() == "a":
    score += 1

print()
print("===== RESULT =====")
print("Score:", score, "/ 5")

if score >= 3:
    print("PASS")
else:
    print("FAIL")