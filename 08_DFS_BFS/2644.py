import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
man1, man2 = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
chk = [False]*(n+1)
visited = []
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(y):
    count = 0
    q = deque([(y)])
    while q:
        e = q.popleft()
        for i in arr[e]:
            if chk[i] == False:
                if count
                chk[i] = True
                q.append(i)

    return -1


print(bfs(man2))
