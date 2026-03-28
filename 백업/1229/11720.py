import sys
input = sys.stdin.readline

N = int(input())
map1 = list(map(int, input().strip())) 

count=0
for i in range(N):
    count+=map1[i]

print(count)