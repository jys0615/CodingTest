import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
result = [0]*N

new_X = list(set(X))
print(new_X)

for i in range(N):
    for j in range(len(new_X)):
        if X[i] > new_X[j]:
            result[i]+=1

for item in result:
    print(item, end=" ")