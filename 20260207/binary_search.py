### 어떤 값을 찾을 때 정렬의 특징으로 빨리 찾음
## 정렬되어 있을 경우, 어떤 값을 찾을 때 : O(N)->O(lgN)
## 처음부터 생각하기 어려움, 쉬운 방법부터 생각

### 1920 ###
"""
1. 아이디어
- N개의 숫자를 정렬
- M개를 for 돌면서, 이진 탐색
- 이진탐색 안에서 마지막 데이터 찾으면 1, 아니면 0

2. 시간복잡도
- N개 입력값 정렬 = O(lgN)
- M개를 N개 중에서 탐색 = O(M * lgN)
- 총합 : O((N+M)lgN) > 가능

3. 자료구조
- N개 숫자 : int[]
- M개 숫자 : int[]
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort()

def search(st, en, target):
    if st == en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    mid = (st+en) // 2
    if nums[mid] < target: # 타겟이 숫자보다 크면 오른쪽
        search(mid+1, en, target)
    else: # 타겟이 숫자보다 작으면 왼쪽
        search(st, mid, target)


for each_target in target_list:
    search(0,N-1, each_target)