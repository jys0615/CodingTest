import sys
input =sys.stdin.readline
x = 9999
y = 9999
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if y % x == 0:
        print('factor')
    elif x % y == 0:
        print('multiple')
    else:
        print('neither')