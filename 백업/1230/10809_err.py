import sys
input = sys.stdin.readline

S = input().rstrip()
check = [-1]*26

for i in range(len(S)):
    if check[ord(S[i])-97] != -1:
        continue
    else:
        check[ord(S[i])-97] = i

for ch in check:
    print(ch, end=" ")