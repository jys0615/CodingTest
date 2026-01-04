import sys
input = sys.stdin.readline

N = int(input())
list = []
for _ in range(N):
    item = int(input())
    list.append(item)

list.sort()
for item in list:
    print(item)