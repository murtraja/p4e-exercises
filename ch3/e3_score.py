try:
    score = float(input("Enter score: "))
except ValueError as e:
    score = -1
if score <0 or score>1:
    print("Bad score")
    exit(0)

if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'
print(grade)