# 10. Cricket Score Analyzer

# Input runs scored in 10 balls.
# Calculate:
# Total Runs
# Strike Rate
# Number of Fours
# Number of Sixes

Runs=[0]*10
six=0
Four=0
Total_Run=0

for i in range(10):
    print("Enter the Run of Ball",i+1,":",end="")
    Runs[i]=int(input())

for i in range(10):
    if Runs[i]==4:
        Four+=1
    if Runs[i]==6:
        six+=1
    Total_Run+=Runs[i]

Strike_Rate= round(Total_Run/10*100,2)

print(f"""
----------Cricket Analyser----------
    Total Four: {Four}
    Total Six: {six}
    Strike Rate: {Strike_Rate}
    Total Run: {Total_Run}
------------------------------------
""")
