import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort() # 이거 하나만으로도 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표 증가순 정렬이 가능!
for i in range(N):
    print(arr[i][0], arr[i][1])