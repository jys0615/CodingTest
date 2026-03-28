import sys
input = sys.stdin.readline

num = int(input().rstrip())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(num))