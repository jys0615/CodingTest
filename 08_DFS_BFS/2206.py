from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

chk = [[[False]*2 for _ in range(M)] for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

# dist를 큐에 같이 넣기
q = deque([(0, 0, 0, 1)])  # y, x, wall, dist
chk[0][0][0] = True

while q:
    y, x, wall, dist = q.popleft()

    if y == N-1 and x == M-1:
        print(dist)
        break

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < N and 0 <= nx < M:
            if arr[ny][nx] == 0 and not chk[ny][nx][wall]:
                chk[ny][nx][wall] = True
                q.append((ny, nx, wall, dist+1))  # dist+1 같이 넣기
            if arr[ny][nx] == 1 and wall == 0 and not chk[ny][nx][1]:
                chk[ny][nx][1] = True
                q.append((ny, nx, 1, dist+1))     # dist+1 같이 넣기
else:
    print(-1)