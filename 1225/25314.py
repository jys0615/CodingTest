import sys
input = sys.stdin.readline

N = int(input())
count = N // 4
str1 = ""
for i in range(count):
    str1+="long "
str1+="int"

print(str1)