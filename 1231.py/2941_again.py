import sys
input = sys.stdin.readline

word = input().rstrip()
check = ["c=", "c-", "dz=", "d-", "lj",
         "nj", "s=", "z="]

for ch in check:
    word = word.replace(ch, "*")

print(len(word))