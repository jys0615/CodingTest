import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
E = int(input())
arr = [[] for _ in range(V+1)]

for i in range(E):
    u,v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u) # 양방향이니까 이것도 해야 함

def bfs(start):
    count = 0
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in arr[v]:
            if not visited[i]:
                count += 1
                queue.append(i)
                visited[i] = True
    return count
visited = [False]*(V+1)
print(bfs(1))