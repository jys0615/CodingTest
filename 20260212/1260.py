import sys
input = sys.stdin.readline
from collections import deque
N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N + 1):
    arr[i].sort()


visited1 = [False] * (N+1) 
visited2 = [False] * (N+1) 
def dfs(v):
    visited1[v] = True
    print(v, end = ' ')
    for i in arr[v]:
        if visited1[i] == False:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited2 = True
    while q:
        item = q.popleft()
        print(item , end = ' ')
        for i in arr[v]:
            if visited2[i] == False:
                visited2[i] = True
                q.append(i)
dfs(V)
print()
bfs(V)