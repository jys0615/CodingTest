import sys
input = sys.stdin.readline

S = input().rstrip() # -> 슬라이싱 가능

list = set()
for i in range(len(S)):
    for j in range(1, len(S)+1):
        list.add(S[i:i+j])
print(len(list))
