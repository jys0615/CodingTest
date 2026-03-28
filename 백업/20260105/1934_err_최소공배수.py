import sys
input = sys.stdin.readline

T = int(input())

while True:
    A, B = map(int, input().split())
    if T == 0:
            break
    for i in range(max(A, B), (A*B)+1):
        if i % A == 0 and i % B == 0:
            print(i)
            T -= 1
            break