import sys
input = sys.stdin.readline

N = int(input())
list = list(map(int, input().split()))
list.sort()
sum = list[0]
result = [0]*N
result[0] = list[0]
for i in range(1, N):
    result[i] = result[i-1]+list[i]
    sum+=result[i]
print(sum)


### 런타임 에러 발생. 왜? 변수명 때문. 앞으로는 arr, prefix_sum으로 할 것
# N = int(input())
# list = list(map(int, input().split()))
# list.sort()
# sum = 0
# result = [0]*N
# for i in range(N):
#     sum+=list[i]
#     result[i] = sum

# print(sum(result))