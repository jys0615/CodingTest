import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
prefix = [0]*(N+1)
# 올바른 방식 - O(N)
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + num[i-1]
for _ in range(M):
    i, j = map(int, input().split())
    if i == j:
        print(num[i-1])
    else:
        print(prefix[j] - prefix[i-1])