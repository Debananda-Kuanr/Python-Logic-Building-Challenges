# 12. Election Voting Machine
# Candidates:
# A
# B
# C
# 10 users can vote.
# At end show:
# Winner
# Total votes
# Percentage of votes


a, b, c = 0, 0, 0

for i in range(10):

    while True:
        print(f"\nVoter {i+1}")

        vote = input("Enter Your Vote (A/B/C): ").lower()

        if vote == "a":
            a += 1
            print("Vote Recorded")
            break

        elif vote == "b":
            b += 1
            print("Vote Recorded")
            break

        elif vote == "c":
            c += 1
            print("Vote Recorded")
            break

        else:
            print("Invalid Candidate")
            print("Please vote again.")

total = a + b + c

print("\n----- Election Result -----")

print(f"Candidate A : {a} votes")
print(f"Candidate B : {b} votes")
print(f"Candidate C : {c} votes")

print(f"\nTotal Votes : {total}")


if total > 0:
    print(f"A Percentage : {(a/total)*100:.2f}%")
    print(f"B Percentage : {(b/total)*100:.2f}%")
    print(f"C Percentage : {(c/total)*100:.2f}%")


if a > b and a > c:
    print("Winner : Candidate A")
    print()

elif b > a and b > c:
    print("Winner : Candidate B")
    print()

elif c > a and c > b:
    print("Winner : Candidate C")
    print()

elif a == b and a > c:
    print("Winner : Both A and B")
    print()

elif b == c and b > a:
    print("Winner : Both B and C")
    print()

elif a == c and a > b:
    print("Winner : Both A and C")
    print()

else:
    print("Winner : Three-way Tie")
    print()