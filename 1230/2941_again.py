import sys
input = sys.stdin.readline

check = ["c=", "c-", "dz=", "d-", "lj", "nj",
        "s=", "z="]

word = input().rstrip()

for ch in check:
    word = word.replace(ch, "*")

print(len(word))