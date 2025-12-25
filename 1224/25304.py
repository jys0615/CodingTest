import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

sum = 0

for i in range(N):
    sum+=map[i][0]*map[i][1] # 실수. N이 아니라 i여야 맞음. 

if X == sum:
    print("Yes")
else:
    print("No")