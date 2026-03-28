import sys
input = sys.stdin.readline

N = int(input())
# 리스트로 감싸야 list[i] 가능.
list = list(map(int, input().split())) 
maxv = max(list)
new_list = []

for i in range(N):
    new_list.append((list[i]/maxv)*100)

result = sum(new_list) / N 
print(result)

# N = int(input())
# list = map(int, input().split()) # list[i] 불가능
# maxv = max(list)
# new_list = []

# print(list)
# for i in range(N):
#     list[i] = list[i]/maxv*100
#     print(list)
