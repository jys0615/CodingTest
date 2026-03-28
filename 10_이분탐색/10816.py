import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))
chk = [0] * M
nums.sort()

def search(st, en, target):
    if st == en:
        return
    mid = (st+en) // 2
    if nums[st] == target:
            chk[st] += 1
    if nums[mid] < target: # 타겟이 숫자보다 크면 오른쪽
        search(mid+1, en, target)
    else: # 타겟이 숫자보다 작으면 왼쪽
        search(st, mid, target)


for each_target in chk:
    search(0,N-1, each_target)
print(chk)