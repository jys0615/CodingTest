import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
pre = [0]
sum = 0

for i in range(N):
    sum += arr[i]
    pre.append(sum)

for i in range(M):
    a, b = map(int, input().split())
    print(pre[b]-pre[a-1])