import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
sum = sum(n for n in range(M, N+1))
minor = [n for n in range(M, N+1)]
for num in range(M, N+1):
    if num == 1:
        sum-=1
        minor.remove(1)
        continue
    for i in range(2, num):
        if num % i == 0: # 소수가 아닌 것을 제거
            sum-=num
            minor.remove(num) # 리스트 삽입은 Append, 삭제는 Remove
            break
if len(minor) == 0:
    print(-1)
else:
    print(sum)
if len(minor) > 0:
    print(min(minor))