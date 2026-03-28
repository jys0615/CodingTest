"""
<BFS - 너비 우선 탐색>
아이디어
1. 시작점에 연결된 Vertex 찾기
2. 찾은 Vertex를 큐에 저장
3. 큐의 가장 먼저 것을 뽑아서 반복

에러
TypeError: unbound method deque.popleft() needs an argument
>> 
"""
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y, x):
    rs = 1
    q = deque([(y, x)])
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    rs += 1
                    q.append((ny, nx))
    return rs



cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if arr[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt+=1
            maxv = max(maxv, bfs(j, i))
print(cnt)
print(maxv)