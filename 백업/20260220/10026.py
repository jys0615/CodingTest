import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(alphabet, y, x, chk):
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey+dy[k]
            nx = ex+dx[k]
            if 0<=ny<N and 0<=nx<N:
                if arr[ny][nx] == alphabet and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny, nx))

chk1 = [[False]*N for _ in range(N)]
count1 = 0
for j in range(N):
    for i in range(N):
        if arr[j][i] == 'R' and chk1[j][i] == False:
            chk1[j][i] = True
            count1+=1
            bfs('R', j, i, chk1)
        elif arr[j][i] == 'G' and chk1[j][i] == False:
            chk1[j][i] = True
            count1+=1
            bfs('G',j, i, chk1)
        elif arr[j][i] == 'B' and chk1[j][i] == False:
            chk1[j][i] = True
            count1+=1
            bfs('B',j, i, chk1)

for j in range(N):
    for i in range(N):
        if arr[j][i] == 'G':
            arr[j][i] = 'R'

chk2 = [[False]*N for _ in range(N)]
count2 = 0
for j in range(N):
    for i in range(N):
        if arr[j][i] == 'R' and chk2[j][i] == False:
            chk2[j][i] = True
            count2+=1
            bfs('R', j, i, chk2)
        if arr[j][i] == 'B' and chk2[j][i] == False:
            chk2[j][i] = True
            count2+=1
            bfs('B',j, i, chk2)

print(count1, count2)