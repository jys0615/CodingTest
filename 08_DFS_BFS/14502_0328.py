import sys
input = sys.stdin.readline
from collections import deque

di = [-1,0,1,0]
dj = [0,1,0,-1]
def bfs(tlst):
    # [0] 3개 좌표를 1로 저장 => 벽 막기
    for i, j in tlst:
        arr[i][j] = 1
    
    cnt = CNT - 3   # 남은 0의 개수 (max값 찾을 변수). 이미 위에서 3개를 1로 지정해서 -3
    # [1] 변수 및 큐 생성, 초기화
    q = deque()
    w = [[0]*M for _ in range(N)] # 방문

    for ti, tj in virus:
        q.append((ti, tj))
        w[ti][tj] = 1 # 방문 체크
    
    # [2] 큐에 데이터 있는 동안 한 개 꺼내서 처리
    while q:
        ci, cj = q.popleft()
        # 4방향, 범위 내, 방문X, 조건 == 0
        for k in range(4): # 4방향
            ni, nj = ci + di[k], cj + dj[k]
            # 범위 내, 방문X, 조건 == 0
            if 0<=ni<N and 0<=nj<M and w[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                w[ni][nj] = 1
                cnt-=1

    # [-1] 3개 좌표를 0로 저장 => 벽 해제. 원상복귀
    for i, j in tlst:
        arr[i][j] = 0
    return cnt  # 남아 있는 0(빈칸) 개수

# def dfs(n, tlst):
#     global ans
#     if n == 3: # 종료조건: 3개 숫자를 모두 선택완료
#         ans = max(ans, bfs(tlst))
#         return
    
#     for j in range(CNT):
#         if v[j] == 0:
#             v[j] = 1
#             dfs(n+1, tlst+[lst[j]])
#             v[j] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = [] # 0의 좌표 저장
virus = [] # 2의 좌표 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            lst.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

CNT = len(lst)
v = [0]*CNT
ans = 0

# [1] 백트래킹으로 풀이: 1000ms
# dfs(0, [])
# print(ans)

# [2] 루프 CNT개 중에서 3개를 선택(가능한 모든 조합) 
# -> 2,3,4개 선택은 이런 루프가 괜찮음
for i in range(CNT-2):
    for j in range(i+1, CNT-1):
        for k in range(j+1, CNT):
            ans = max(ans, bfs([lst[i], lst[j], lst[k]]))

print(ans)