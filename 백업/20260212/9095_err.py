import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] * (N+1)
    for i in range(1, N+1):
        if i == 1:
            arr[i] = 1
        elif i == 2:
            arr[i] = 2
        elif i == 3:
            arr[i] = 4
        else:
            arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
    print(arr[N])

### 본인이 작성한 오답 코드 ###
# T = int(input())
# for t in range(T):
#     item = int(input())
#     arr = [0]*item
#     arr[0] = 1
#     arr[1] = 2
#     arr[2] = 4
#     if item <= 3:
#         print(arr[item-1])
#         continue
#     else:
#         for i in range(3, item):
#             arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
#     print(arr[item-1])