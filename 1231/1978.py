import sys
input = sys.stdin.readline

N = int(input())
minor = list(map(int, input().split()))
sum = N

for i in range(N):
    if minor[i] == 1:
        sum-=1
        continue
    for j in range(2, minor[i]):
        if minor[i] % j == 0:
            sum-=1
            break

print(sum)