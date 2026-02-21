import sys
input = sys.stdin.readline
from collections import deque
T = int(input())

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    q = deque([(y, x)])
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey+dy[k]
            nx = ex+dx[k]
            if 0<=ny<N and 0<=nx<M:
                if arr[ny][nx] == 1 and chk[ny][nx] == False: # 있어야 함. 아니면 인덱스 범위 초과 에러
                    chk[ny][nx] = True
                    q.append((ny, nx))


for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    chk = [[False]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    count = 0
    for j in range(N): # 세로->y
        for i in range(M): # 가로->x
            if arr[j][i] == 1 and chk[j][i] == False:
                chk[j][i] = True
                count+=1
                bfs(j, i)
    print(count)
 



