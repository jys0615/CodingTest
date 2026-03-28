import sys
input = sys.stdin.readline
from itertools import permutations
N, M = map(int, input().split())

iter = []
for i in range(N):
    iter.append(i+1)
for i in permutations(iter, M):
    for j in range(M):
        print(i[j], end = ' ')
    print()