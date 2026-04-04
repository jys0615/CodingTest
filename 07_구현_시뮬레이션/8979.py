import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nation = [[0]*3 for _ in range(N+1)]
for _ in range(N):
    i, g, s, b = list(map(int, input().split()))
    nation[i] = g, s, b

nation = sorted(nation, key = lambda x: (x[0], x[1], x[2]), reverse=True)

print(nation)