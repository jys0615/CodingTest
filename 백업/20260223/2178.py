import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]
chk = [[False]*M for _ in range(N)]
def bfs(y, x):
    q = deque([(y, x)])
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if arr[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    arr[ny][nx] += arr[ey][ex]
                    q.append((ny, nx))

bfs(0, 0)
print(arr[N-1][M-1])