import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
sy, sx = 0, 0
for j in range(n):
    for i in range(m):
        if arr[j][i] == 2:
            sy, sx = j, i

q = deque([(sy, sx)])
dist[sy][sx] = 0

while q:
    ey, ex = q.popleft()
    for k in range(4):
        ny = ey + dy[k]
        nx = ex + dx[k]
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[ey][ex] + 1
                q.append((ny, nx))

for j in range(n):
    for i in range(m):
        print(dist[j][i], end=" ")
    print()