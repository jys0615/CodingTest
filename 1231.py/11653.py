import sys
input = sys.stdin.readline

N = int(input())
result = []
i = 2
while N > 1: # True로도 가능
    # if N == 1: # True일 때 필요
    #     break
    if N % i == 0:
        N = N // i
        print(i)
    else:
        i+=1