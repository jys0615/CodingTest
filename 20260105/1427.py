import sys
input = sys.stdin.readline

N = list(input().rstrip())
order = [0]*len(N)
for i in range(len(N)):
    order[i] = int(N[i])
order.sort(reverse=True)
for o in order:
    print(o, end="")