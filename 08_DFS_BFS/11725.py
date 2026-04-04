import sys
input = sys.stdin.readline

N = int(input())

arr = [0]*(N+1)

for _ in range(N-1):
    y, x = map(int, input().split())
    arr[y].append(x)

