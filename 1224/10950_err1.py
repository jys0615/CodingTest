import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
# 리스트 기준 map으로 여러 입력 받기->DFS/BFS에서도 사용될 예정

for i in range(N):
    print(map[i][0]+map[i][1])