import sys
input = sys.stdin.readline

H, M = map(int, input().split())
plus = int(input())
total = 60*H+M+plus

if total >= 1440: ## 주의! 00:00도 포함을 해야 한다.
    total = total - 1440

new_H = total//60
new_M = total%60
print(new_H, new_M)