import sys
input = sys.stdin.readline

chess = list(map(int, input().split()))
answer = [1,1,2,2,2,8]
for ch, ans in zip(chess, answer):
    print(ans-ch, end=" ")