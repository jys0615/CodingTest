import sys
input = sys.stdin.readline

grade = {
    "A+" : 4.5, "A0" : 4.0,
    "B+" : 3.5, "B0" : 3.0,
    "C+" : 2.5, "C0" : 2.0,
    "D+" : 1.5, "D0" : 1.0,
    "F" : 0.0
}

report = [list(input().split()) for _ in range(20)]

credit_sum = 0.0
sum = 0.0
for name, credit, gr in report:
    if gr == "P":
        continue
    else:
        credit_sum += float(credit) * float(grade[gr])
    sum += float(credit)

print("%.6f" %(credit_sum / sum))