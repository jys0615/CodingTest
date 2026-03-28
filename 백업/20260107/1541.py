import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        stack.append(cmd[1])
    elif cmd[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 4:
        if len(stack) == 0:
                    print(1)
        else:
             print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1]) # 맨 위 정수

            
