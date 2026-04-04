import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(H+X)]

for j in range(H + X):
    for i in range(W + Y):
        B[i][j]-=B[i-X][j-Y]

