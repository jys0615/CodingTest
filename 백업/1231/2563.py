import sys
input = sys.stdin.readline

N = int(input())

arr = [[0]*2 for _ in range(N)]
maxx = 0
maxy = 0
for i in range(0, N):
    x, y = map(int, input().split())
    arr[i][0], arr[i][1] = x, y
    if maxx < arr[i][0]:
        maxx = arr[i][0]
    if maxy < arr[i][1]:
        maxy = arr[i][1]

max_square = (maxx+10)*maxy
print(maxx, maxy)
