import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
chk = [False]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def bfs(start):
    q = deque([(start)])
    while q:
        v = q.popleft()
        for i in arr[v]:
            if chk[i] == False:
                chk[i] = True
                q.append(i)

count = 0
for i in range(1, N+1):
    if chk[i] == False:
        chk[i] = True
        count+=1
        bfs(i)

print(count)