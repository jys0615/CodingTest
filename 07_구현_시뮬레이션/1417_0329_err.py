import sys
input = sys.stdin.readline

N = int(input())
dasom = int(input())
count=0
member = []
for _ in range(N-1):
    member.append(int(input().rstrip()))
if N == 1:
    print(0)
else:
    while dasom <= max(member):
        dasom+=1
        count+=1
        member[member.index(max(member))]-=1
    print(count)