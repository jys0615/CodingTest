import sys
input = sys.stdin.readline

N = int(input().rstrip())
result = 0
str1 = str(N)
for i in range(len(str1)):
    result += int(str1[i])
print(N + result)