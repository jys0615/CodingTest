import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0
cost = []
for _ in range(N):
    A, B = map(int, input().split())
    cost.append(B-A)

cost.sort()
if cost[K-1]<0:
    print(0)
else:
    print(cost[K-1])