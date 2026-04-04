import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    sum = 0
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(y1-1, y2):
        for i in range(x1-1, x2):
            sum += arr[j][i]
    print(sum)