import sys
input = sys.stdin.readline
from collections import deque
INF = float('inf')
def bfs_01(sy, sx):
    dist = [[INF]*M for _ in range(N)]
    dist[sy][sx] = 0
    dq = deque([(sy, sx)])

    while dq:
        y, x = dq.popleft()
        for dy, dx, cost in moves:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<M:
                new_dist = dist[y][x] + cost
                if new_dist < dist[ny][nx]:
                    dist[ny][nx] = new_dist
                    if cost == 0:
                        dq.appendleft((ny, nx))
                    else:
                        dq.append((ny, nx))
    return dist[N-1][M-1]
