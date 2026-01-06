import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(input().rstrip())
arr.sort() # 알파벳 기준으로 우선 정렬
arr.sort(key = lambda x: len(x)) # 특정 기준을 지정하여 정렬

print(arr)