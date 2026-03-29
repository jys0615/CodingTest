import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs(y, x):

    q = deque([(y, x)])
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if maze[ny][nx] == 1:
                    maze[ny][nx] += maze[ey][ex]
                    q.append((ny, nx))

    return maze[N-1][M-1]


print(bfs(0, 0))