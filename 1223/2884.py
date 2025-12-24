import sys
input = sys.stdin.readline

H, M = map(int, input().split())

total = H*60+M
out = total - 45

if out < 0:
    out = 1440 + out

new_H = out // 60
new_M = out % 60

print(new_H, new_M)