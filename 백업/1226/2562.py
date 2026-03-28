import sys
input = sys.stdin.readline

arr = [0]*9
for i in range(9):
    arr[i] = int(input())

max = 0
index = 0
for i in range(9):
    if max < arr[i]:
        max = arr[i]
        index = i

print(max, index+1)