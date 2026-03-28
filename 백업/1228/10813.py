import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [n for n in range(1,N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for data in basket:
    print(data, end=" ")