import sys
input = sys.stdin.readline

n1=n2=n3=n4=n5=n6=0

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

di, dj = [0,0,0,-1,1], [0,1,-1,0,0] # 인덱스 0은 안 쓰고, 동 서 북 남
ans = []
for cmd in command:
    ni, nj = x + di[cmd], y + dj[cmd]
    if 0<=ni<N and 0<=nj<M:
        if cmd == 1:     # 동
            n1,n3,n4,n6 = n4,n1,n6,n3
        elif cmd == 2:   # 서
            n1,n3,n4,n6 = n3,n6,n1,n4
        elif cmd == 3:   # 북
            n1,n2,n5,n6 = n5,n1,n6,n2
        else:           # 남
            n1,n2,n5,n6 = n2,n6,n1,n5

        if arr[ni][nj] == 0:
            arr[ni][nj] = n6
        else: # 바닥이 0이 아니면
            n6, arr[ni][nj] = arr[ni][nj], 0

        ans.append(n1) # 윗면의 값을 ans에 추가
        x, y = ni, nj  # 이동처리

print(*ans, sep='\n')