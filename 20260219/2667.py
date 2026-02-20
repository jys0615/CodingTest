import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
rs = []
chk = [[False]*N for _ in range(N)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y, x):
    q = [(y, x)]
    sum = 1
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey+dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<N:
                if arr[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    sum+=1
                    q.append((ny, nx))
    return sum

cnt = 0
for j in range(N):
    for i in range(N):
        if arr[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            rs.append(bfs(j, i))
            cnt+=1

print(cnt)
rs.sort()
for item in rs:
    print(item)