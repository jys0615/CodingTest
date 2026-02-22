import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
M = int(input())
chk = list(map(int, input().split()))

def search(st, en, target):
    count = 0
    data.sort()
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            count+=1 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    print(count)

for item in chk:
    search(0, N-1, item)
