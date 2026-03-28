import sys
input = sys.stdin.readline

list = []

for _ in range(5):
    item = int(input())
    list.append(item)

print(sum(list) // 5)
list.sort()
print(list[2])