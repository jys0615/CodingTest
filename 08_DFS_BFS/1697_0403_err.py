from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [-1]*100001
visited[N] = 0
def bfs(num):
    q = deque([num])
    while q:
        ey = q.popleft()
        if ey == K:
            print(visited[ey])
            break
        for k in [ey-1, ey+1, ey*2]:
            if 0<=k<=100000 and visited[k] == -1:
                visited[k] = visited[ey]+1
                q.append(k)

bfs(N)