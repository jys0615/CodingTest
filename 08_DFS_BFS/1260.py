import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

# 인접 리스트 만들기
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 번호가 작은 정점부터 방문해야 하므로 정렬
for i in range(1, N + 1):
    arr[i].sort()

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for nxt in arr[v]:
        if not visited1[nxt]:
            dfs(nxt)

def bfs(v):
    q = deque([v])
    visited2[v] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in arr[cur]:
            if not visited2[nxt]:
                visited2[nxt] = True
                q.append(nxt)

dfs(V)
print()
bfs(V)