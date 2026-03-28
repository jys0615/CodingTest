import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
new_arr = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        new_arr[i][j] = A[i][j]+B[i][j]
for i in range(N):
    for j in range(M):
        if j == 2:
            print(new_arr[i][j])
        else:
            print(new_arr[i][j], end=" ")

### new_arr = [] 한 상태에서 slice 즉, new_arr[i][j] 활용은 불가!