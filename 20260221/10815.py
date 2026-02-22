import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
M = int(input())
chk = list(map(int, input().split()))

def search(st, en, target):
    if st == en:
        if data[st] == target:
            return 1
        else:
            return 0
    mid = (st+en) // 2
    if data[mid] < target:
        return search(mid+1, en, target)
    else:
        return search(st, mid, target)
        
data.sort()
for item in chk:
    result = search(0, N-1, item)
    print(result, end=' ')