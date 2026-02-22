import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    arr[u].sort()
    arr[v].sort()

visited1 = [False]*(N+1)
visited2 = [False]*(N+1)

def dfs(v):
    visited2[v] = True
    print(v, end= ' ')
    for i in arr[v]:
        if visited2[i] == False:
            visited2[i] = True
            dfs(i)
from collections import deque
def bfs(v):
    q = deque([(v)])
    visited1[v] = True
    while q:
        e = q.popleft()
        print(e, end=' ')
        for i in arr[e]:
            if visited1[i] == False:
                visited1[i] = True
                q.append(i)


dfs(V)
print()
bfs(V)