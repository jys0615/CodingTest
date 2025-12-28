import sys
input = sys.stdin.readline

N = int(input())
map = list(map(int, input().split()))

print(min(map),max(map)) # 두 함수 시간 복잡도 : O(n)