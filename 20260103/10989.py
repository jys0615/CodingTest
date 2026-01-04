import sys
input =sys.stdin.readline

N = int(input())
list = []
for _ in range(N):
    item = int(input())
    list.append(item)

for i in range(N-1):
    for j in range(i+1, N):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
for item in list:
    print(item)