import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
copy = [row[:] for row in A]
# -1은 청정기가 설치된 곳, 나머지는 미세먼지양

for _ in range(T):
    # 1. 미세먼지가 확산
    for j in range(R):
        for i in range(C):
            if copy[j][i] > 0:          # 원본 기준으로 판단
                for k in range(4):
                    ny = j + dy[k]
                    nx = i + dx[k]
                    if 0 <= ny < R and 0 <= nx < C and copy[ny][nx] != -1:
                        amount = copy[j][i] // 5   # 원본 기준으로 확산량 계산
                        A[ny][nx] += amount
                        A[j][i] -= amount    
    
for item in A:
    print(item)