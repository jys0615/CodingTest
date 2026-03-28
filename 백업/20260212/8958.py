import sys
input = sys.stdin.readline

T = int(input())
rs = [list(input().strip()) for _ in range(T)]

for item in rs:
    sum = 0
    repeat = 1
    for i in range(len(item)):
        if item[i] == 'O':
            sum += repeat
            repeat += 1
        else:
            repeat = 1
    print(sum)