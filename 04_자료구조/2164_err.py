import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
queue = deque()
for i in range(N):
    queue.append(i+1)

# while True: # 이 구조대로라면 N = 1일 때 브레이크가 안 걸림
#     queue.popleft()
#     if len(queue) == 1:
#         break
#     item = queue.popleft()
#     queue.append(item)

# print(queue[0])

while len(queue) > 1: 
    queue.popleft()
    # item = queue.popleft()
    # queue.append(item)
    queue.append(queue.popleft())

print(queue[0])