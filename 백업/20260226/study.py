### 완전탐색 및 백트래킹 ###

## 1. 순열 순서 O, 중복 X ##

def permutation(arr, r): # 순서는 있으나 중복은 아님
    # 1,2->2,1->1,3->,,,
    result = []
    used = [False] * len(arr)
    path = []
    def dfs():
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                dfs()
                path.pop() # 되돌아오기 -> 백트래킹
                used[i] = False
    
    dfs()
    return result

## 2. 조합 (순서 X, 중복 X) ##
def combination(arr, r): # 순서랑 중복 둘 다 X
    # 1,2->1,3->2,3->,,,
    result = []
    path = []

    def dfs(start):
        if len(path) == r:
            result.append(path[:])
            return
        
        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(i+1) # i+1: 같은 원소 다시 안 쓰기
            path.pop()
    dfs(0)
    return result

## 3. 중복 순열 (순서 O, 중복 O) ##
def repeat_permutation(arr, r): # 순서 중복 다 있음 
    # 1,1->1,2->2,2->,,,
    result = []
    path = []

    def dfs():
        if len(arr) == r:
            result.append(path[:])
            return 
        
        for i in range(len(arr)):
            path.append(arr[i])
            dfs() # used 없음 ! 중복 허용
            path.pop()

    dfs()
    return result