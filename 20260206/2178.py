import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
# chk = [[False]*M for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]


def bfs(y, x):
    q = deque()                                       
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if arr[ny][nx] == 0:
                    continue
                if arr[ny][nx] == 1:
                    arr[ny][nx] = arr[ey][ex]+1
                    q.append((ny, nx))
    return arr[N-1][M-1]

print(bfs(0,0))