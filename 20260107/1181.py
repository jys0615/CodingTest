import sys
input = sys.stdin.readline

N = int(input())
arr = set()

for i in range(N):
    item = input().rstrip()
    arr.add(item)
arr = list(arr)
arr.sort()
arr.sort(key = lambda x : len(x))

for item in arr:
    print(item)