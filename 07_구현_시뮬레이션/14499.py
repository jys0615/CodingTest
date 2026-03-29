import sys
input = sys.stdin.readline

N, M, ci, cj, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # 지도
cmd = list(map(int, input().split())) # 동서북남 이동 명령

n1=n2=n3=n4=n5=n6=0 
#         [ n2 ] ← 북쪽 면
# [ n4 ] [ n1 ] [ n3 ] ← 펼친 모양 (n1=위, n4=서, n3=동)
#         [ n5 ] ← 남쪽 면
#         [ n6 ] ← 아래 면 (바닥에 닿는 면)
di, dj = [0,0,0,-1,1], [0,1,-1,0,0] # 인덱스 0은 안 쓰고, 동 서 북 남
ans = []
for dr in cmd: # 각각의 명령에 대해서 처리
    ni, nj = ci + di[dr], cj + dj[dr] # 각 명령에 대해 이동처리
    if 0<=ni<N and 0<=nj<M:
        if dr == 1:     # 동
            n1,n3,n4,n6 = n4,n1,n6,n3
        elif dr == 2:   # 서
            n1,n3,n4,n6 = n3,n6,n1,n4
        elif dr == 3:   # 북
            n1,n2,n5,n6 = n5,n1,n6,n2
        else:           # 남
            n1,n2,n5,n6 = n2,n6,n1,n5

    # [3] 이동한 바닥판이 0인지 여부에 따라 처리
    if arr[ni][nj] == 0: # 바닥이 0이면
        arr[ni][nj] = n6 # 주사위 아랫면 값을 바닥에 복사
    else: # 바닥이 0이 아니면
        n6, arr[ni][nj] = arr[ni][nj], 0 # 바닥값을 주사위로, 바닥 0으로 초기화

    ans.append(n1) # 윗면의 값을 ans에 추가
    ci, cj = ni, nj  # 이동처리
    
print(*ans, sep='\n')