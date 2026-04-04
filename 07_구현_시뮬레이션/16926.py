import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

out_A = deque([])
in_A = deque([])
for j in range(N):
    for i in range(M):
        if i == 0 or i == N-1 or j == 0 or j == M-1:
            out_A.append(A[j][i])
        else:
            in_A.append(A[j][i])
print(in_A)
