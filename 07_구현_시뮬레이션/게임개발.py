import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chk = [[False]*M for _ in range(N)]
chk[A][B] = 1

dy = [-1,0,1,0]
dx = [0,1,0,-1]

count = 1
turn = 0

while True:
    d -= 1
    if d == -1:
        d = 3
    ny = B + dy[d]
    nx = A + dx[d]
    if chk[ny][nx] == 0 and arr[ny][nx] == 0:
        chk[ny][nx] = 1
        B = ny
        A = nx
        count+=1
        turn = 0
        continue
    else:
        turn+=1

    if turn == 4:
        ny = B - dy[d]
        nx = A - dx[d]

        if arr[ny][nx] == 0:
            B = ny
            A = nx
        else:
            break
        turn = 0
print(count)