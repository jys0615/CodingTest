from collections import deque
import sys
input = sys.stdin.readline

wheel = [deque(map(int, input().strip())) for _ in range(4)]

K = int(input().rstrip())

for _ in range(K):
    wheel_num, direction = map(int, input().split())

    if direction == 1:
        target = wheel_num-1
        left = target-1 # 왼쪽 톱
        right = target+1 # 오른쪽 톱
        if 0<=left<4:
            if wheel[left][2] != wheel[target][6]:
                item = wheel[left].popleft()
                wheel[left].append(item)
        if 0<=right<4:
            if wheel[right][6] != wheel[target][2]:
                item = wheel[right].popleft()
                wheel[right].append(item)
         
        item = wheel[target].pop()
        wheel[target].appendleft(item)

    elif direction == -1:
        target = wheel_num-1
        left = target-1 # 왼쪽 톱
        right = target+1 # 오른쪽 톱
        if 0<=left<4:
            if wheel[left][2] != wheel[target][6]:
                item = wheel[left].pop()
                wheel[left].appendleft(item)
        if 0<=right<4:
            if wheel[right][6] != wheel[target][2]:
                item = wheel[right].pop()
                wheel[right].appendleft(item)
         
        item = wheel[target].popleft()
        wheel[target].append(item)

sum = 0
if wheel[0][0] == 1:
    sum+=1

if wheel[1][0] == 1:
    sum+=2

if wheel[2][0] == 1:
    sum+=4

if wheel[3][0] == 1:
    sum+=8

print(sum)