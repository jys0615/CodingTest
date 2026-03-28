import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    h = int(input())
    stack.append(h)

max = 0
count = 0
for i in range(N-1, -1, -1):
    if stack[i] > max:
        max = stack[i]
        count +=1

print(count)