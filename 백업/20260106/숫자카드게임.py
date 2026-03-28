import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0]*N
for i in range(N):
    result[i] = min(arr[i])
print(max(result))
