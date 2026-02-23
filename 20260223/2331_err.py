import sys
input = sys.stdin.readline

A, P = map(int, input().split())
arr = [A]
i = 1
while 1:
    stack = [] # 숫자를 슬라이싱할 때 사용
    str1 = str(arr[i-1])
    for item in str1:
        rs = int(item)
        stack.append(rs)
    sum = 0
    for item in stack:
        sum+=pow(item, P)
    if sum in arr:
        print(arr.index(sum))
        break
    arr.append(sum)
    i+=1