# def permutation(arr, r): # 순서는 있으나 중복은 아님
#     # 1,2->2,1->1,3->,,,
#     result = []
#     used = [False] * len(arr)
#     path = []
#     def dfs():
#         if len(path) == r:
#             result.append(path[:])
#             return
#         for i in range(len(arr)):
#             if not used[i]:
#                 used[i] = True
#                 path.append(arr[i])
#                 dfs()
#                 path.pop() # 되돌아오기 -> 백트래킹
#                 used[i] = False
    
#     dfs()
#     return result

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
chk = [False]*N
path = []
result = []
def dfs():
    if len(path) == M:
        result.append(path[:]) # 복사본을 저장하여 path 변경 영향 받지 않게 한다.
        return
    for i in range(len(arr)):
        if not chk[i]:
            chk[i] = True
            path.append(arr[i])
            dfs()
            path.pop()
            chk[i] = False
dfs()
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end= " ")
    print()