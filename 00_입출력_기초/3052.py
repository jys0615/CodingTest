import sys
input = sys.stdin.readline
list = []
for i in range(0, 10):
    n = int(input())
    list.append(n % 42)

check = []
count=0
for data in list:
    if data not in check:
        count+=1
        check.append(data)
print(count)