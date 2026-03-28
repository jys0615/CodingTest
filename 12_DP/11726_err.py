import sys
input = sys.stdin.readline

sum = [0,1,2] # 헷갈리지 않게 인덱스 0은 0으로 처리
n = int(input())
for i in range(3, n+1):
    sum.append((sum[i-1]+sum[i-2])%10007)
print(sum[n])



#### n이 최대 1000인데 같은 값을 재귀로 계산하면 터진다.
# def recur(num):
#     if num == 1:
#         return 1
#     elif num == 2:
#         return 2
#     else:
#         return recur(num-1)+recur(num-2)

# n = int(input())
# print(recur(n) % 10007)