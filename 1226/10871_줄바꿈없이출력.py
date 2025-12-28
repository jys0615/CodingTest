import sys
input = sys.stdin.readline

N, X = map(int, input().split())
map = list(map(int, input().split()))

for val in map:
    if val < X:
        print(val, end=" ") # 이렇게 하면 줄바꿈 없이 출력 가능