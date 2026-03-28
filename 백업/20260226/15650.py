# ## 2. 조합 (순서 X, 중복 X) ##
# def combination(arr, r): # 순서랑 중복 둘 다 X
#     # 1,2->1,3->2,3->,,,
#     result = []
#     path = []

#     def dfs(start):
#         if len(arr) == r:
#             result.append(path[:])
#             return
        
#         for i in range(start, len(arr)):
#             path.append(arr[i])
#             dfs(i+1) # i+1: 같은 원소 다시 안 쓰기
#             path.pop()
#     dfs(0)
#     return result

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
result = []
path = []

def dfs(start):
    if len(path) == M:
        result.append(path[:])
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        dfs(i+1)
        path.pop()

dfs(0)

for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end= " ")
    print()