'''
어떤 값을 찾을 때 정렬의 특징을 이용해 빨리 찾는다
정렬되어 있을 경우, 어떤 값을 찾을 때 : O(N) -> O(lgN)
처음부터 생각하기 어려워서 쉬운 방법부터 생각해라
'''

### 1920 ###
def search(st, en, target):
    if st == en:
        if arr[st] == target:
            return 1
        else:
            return 0
    mid = (st+en) // 2 ## 0이랑 5면 2를 선택한다
    if arr[mid] < target:
        return search(mid+1, en, target)
    else:
        return search(st, mid, target)

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
chk = list(map(int, input().split()))
arr.sort()
for item in chk:
    result = search(0, N-1, item)
    print(result)
