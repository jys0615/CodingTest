import sys
input = sys.stdin.readline
x=9
y=9
while 1:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    print(x+y)