import sys
input = sys.stdin.readline

### 이럴 때 사용하는 것이 계수정렬 ###
N = int(input())
arr = []
for i in range(N):
    item = int(input())
    arr.append(item)

count = [0] * (max(arr)+1)
for i in range(len(arr)):
    count[arr[i]] += 1
print(count)
for i in range(len(count)):
    for j in range(count[i]):
        print(i)

### 메모리 초과 발생 ###
# N = int(input())

# arr = []

# for i in range(N):
#     item = int(input())
#     arr.append(item)
# arr.sort()
# print(arr)