import sys
input = sys.stdin.readline

arr = [list(input().split()) for _ in range(20)]
grade = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5,
         "B0" : 3.0, "C+" : 2.5, "C0" : 2.0,
         "D+" : 1.5, "D0" : 1.0, "F" : 0.0}

sum = 0.0
sum_credit = 0.0

for i in range(20):
    if arr[i][2] == "P":
        continue
    sum_credit += float(arr[i][1])
for j in range(20):
    if arr[j][2] == "P":
        continue
    else:
        sum += float(arr[j][1]) * grade[arr[j][2]]

print(sum / sum_credit)
# print('%.6f' % (sum / sum_credit))