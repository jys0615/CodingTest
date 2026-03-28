import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)


def bfs(u):
    q = [(u)]
    while q:
        e = q.pop()
        for i in arr[e]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)

for _ in range(M):
    u,v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

count = 0
for i in range(1, N+1):
    if visited[i] == False:
        visited[i] = True
        bfs(i)
        count+=1

print(count)