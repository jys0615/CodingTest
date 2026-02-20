import sys
input = sys.stdin.readline

n = int(input())
rs = [list(map(int, input().split())) for _ in range(n)]

for k in range(n): # 거치는 값
    for j in range(n): # 시작
        for i in range(n): # 도착
            if rs[j][k] == 1 and rs[k][i] == 1:
                rs[j][i] = 1

for i in range(n):
    for j in range(n):
        print(rs[i][j], end=' ')
    print()