import sys
input = sys.stdin.readline

N, K = map(int, input().split())
list = [0]*N
for i in range(N):
    item = int(input())
    list[i] = item


count = 0
i = N-1
while i > -1:
    if list[i] > K:
        i-=1
        continue
    else:
        K = K - list[i]
        count+=1
print(count)