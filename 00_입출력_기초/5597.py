import sys
input = sys.stdin.readline

attend = [n for n in range(1,31)]
check = [0]*30

while 1:
    try:
       student = int(input())
       check[student-1] = 1
    except: # 예외 처리
        break

for i, data in enumerate(check):
    if data == 0:
        print(i+1)