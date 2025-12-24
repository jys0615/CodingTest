import sys
input = sys.stdin.readline

A, B = map(int, input().split())

print(A+B)


# AttributeError: 'builtin_function_or_method' object has no attribute 'split'
# input도 ()이 필요하다.