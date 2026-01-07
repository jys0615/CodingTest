import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
X_prime = [0]*N
sorted_X = list(set(X))
for i in range(N):
    for j in range(len(sorted_X)):
        if X[i] > sorted_X[j]:
            X_prime[i] += 1


    
for item in X_prime:
    print(item, end= " ")