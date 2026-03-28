import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
maxv = -1 # 최댓값도 디폴트는 0이 아닌 -1로 할 것. 0이 최대일 수도
ansi = 0
ansj = 0
for i in range(9):
    for j in range(9):
        if maxv < arr[i][j]:
            maxv = arr[i][j]
            ansi = i
            ansj = j

print(maxv)
print(ansi+1, ansj+1) 
