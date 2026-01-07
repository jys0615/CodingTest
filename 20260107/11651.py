import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x : x[0])
print(arr)
arr.sort(key = lambda x : x[1])

for i in range(N):
    print(arr[i][0], arr[i][1])