import sys
from collections import deque
input = sys.stdin.readline

dy = [-2,-1,1,2,2,1,-1,-2]
dx = [1,2,2,1,-1,-2,-2,-1]
def bfs(y, x):
    dist = [[-1]*I for _ in range(I)] # dist로 하면 리턴할 때 더 용이
    dist[y][x] = 0
    q = deque([(y, x)])
    while q:
        ey, ex = q.popleft()
        for k in range(8):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<I and 0<=nx<I:
                if dist[ny][nx] == -1:
                    dist[ny][nx] = dist[ey][ex] + 1
                    if ny == end[0] and nx == end[1]:
                        return dist[ny][nx]  # 초기값이 1이라서 -1   
                    q.append((ny, nx))
    


T = int(input())
for _ in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    if start[0]==end[0] and start[1]==end[1]: # 시작과 도착이 같은 엣지 케이스
        print(0)
    else:
        print(bfs(start[0], start[1]))