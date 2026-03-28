import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
max_value = 0
min_value = sys.maxsize
for i in range(N):
    for j in range(N):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
        if arr[i][j] < min_value:
            min_value = arr[i][j]

def bfs(y, x):
    q = deque([(y, x)])
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<N:
                if chk[ny][nx] == False and arr[ny][nx] > h:
                    chk[ny][nx] = True
                    q.append((ny, nx))


maxv = 0
for h in range(0, max_value):
    count = 0
    chk = [[False]*N for _ in range(N)]

    for j in range(N):
        for i in range(N):
            if arr[j][i] > h and chk[j][i] == False:
                count += 1
                chk[j][i] = True
                bfs(j, i)
    if count > maxv:
        maxv = count
    
print(maxv)