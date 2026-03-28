import sys
input = sys.stdin.readline

L = int(input())
str1 = list(input().strip())
mod = 1234567891
sum = 0
for l in range(L):
    sum += (ord(str1[l]) - 96) * pow(31, l)

print(sum % mod)

## ord : A -> 65
## chr : 65 -> A