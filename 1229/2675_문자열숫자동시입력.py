import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    R, S = input().split()
    new_list = ""
    for i in range(0, len(S)):
        new_list+=S[i]*int(R)
    print(new_list)