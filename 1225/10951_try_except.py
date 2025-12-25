import sys
input = sys.stdin.readline
while 1:
    try:
        a, b =map(int, input().split())
        print(a+b)
    except: # 예외 처리
        break