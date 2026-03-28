import sys
input = sys.stdin.readline

T = int(input().rstrip())
dy = [0,1,0,-1]
dx = [1,0,-1,0]
from collections import deque
def bfs(start):
    q = deque([start])
    while q:
        v = q.popleft()
        for i in arr[v]:
            if chk[i] == False:
                chk[i] = True
                q.append(i)


for _ in range(T):
    N = int(input().rstrip())
    arr = [[] for _ in range(N+1)]
    item = list(map(int, input().split()))
    chk = [False]*(N+1) # []로 감싸면 외부 리스트 길이가 1이 되어서 에러 발생
    count = 0
    for i in range(1, N+1):
        arr[i].append(item[i-1])

    for i in range(1, N+1):
        if chk[i] == False:
            count += 1
            chk[i] = True
            bfs(i)
    print(count)