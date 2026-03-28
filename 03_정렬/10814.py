import sys
input = sys.stdin.readline

N = int(input())
member = [list(input().split()) for _ in range(N)]

member.sort(key = lambda x: int(x[0]))

for mb in member:
    print(mb[0], mb[1])