import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))
minv = sys.maxsize
maxv = -sys.maxsize

def dfs(n, temp):
    global minv, maxv

    if n == N-1:
        maxv = max(temp, maxv)
        minv = min(temp, minv)
        return

    if operator[0] != 0:
        operator[0] -= 1
        dfs(n+1, temp + A[n+1])
        operator[0] += 1
    if operator[1] != 0:
        operator[1] -= 1
        dfs(n+1, temp - A[n+1])
        operator[1] += 1
    if operator[2] != 0:
        operator[2] -= 1
        dfs(n+1, temp * A[n+1])
        operator[2] += 1
    if operator[3] != 0:
        operator[3] -= 1
        dfs(n+1, temp // A[n+1])
        operator[3] += 1

dfs(0, A[0])
print(maxv)
print(minv)