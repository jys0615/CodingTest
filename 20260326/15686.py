import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 0은 빈 칸, 1은 집, 2는 치킨집
