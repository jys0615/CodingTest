import sys
input = sys.stdin.readline
from collections import deque
N = int(input().rstrip())
K = int(input().rstrip())
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    j, i = map(int, input().split())
    arr[j-1][i-1] = 1
L = int(input().rstrip())
direction = deque([])
distance = deque([])
for _ in range(L):
    X, C = input().split()
    direction.append(C)
    distance.append(int(X))

def count(y, x, direction, distance):
    arr[y][x] = 2
    current_dis = distance.popleft()
    for i in range(1, current_dis+1):
        arr[y][x+i] = 2
        cur_y = y
        cur_x = x+i
    for i, item in enumerate(direction):
        if i > len(distance)-1:
            break
        if item == "D":
            j = 0
            while j < distance[i]:
                if cur_y > N-1 or cur_x > N-1:
                    break
                arr[cur_y][cur_x] = 2
                # print(cur_y, cur_x)
                cur_x=cur_x+1
                j+=1
            
        elif item == "L":
            k = 0
            while k < distance[i]:
                if cur_y > N-1 or cur_x > N-1:
                    break
                arr[cur_y][cur_x] = 2
                cur_y=cur_y+1
                k+=1


result = count(0, 0, direction, distance)
print(arr)
