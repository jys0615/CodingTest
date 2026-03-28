import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
rs = []
dy = [0,1,0,-1]
dx = [1,0,-1,0]
chk = [[False]*N for _ in range(N)]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if arr[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)


cnt = 0
for j in range(N):
    for i in range(N):
        if arr[j][i] == 1 and chk[j][i] == False:
            cnt+=1
            chk[j][i] = True
            each = 0
            dfs(j, i)
            rs.append(each)
print(cnt)
rs.sort()
for item in rs:
    print(item)