import sys
input =sys.stdin.readline

N = int(input())
sang = list(map(int, input().split())) # []로 감싸면 2차원 배열 간주?
M = int(input())
check = list(map(int, input().split()))
sang.sort()
# check.sort()
result = [0]*M
for i in range(m):
    if m_arr[i] in arr : 
        print(1,end=' ')
    else : print(0,end=' ')

# N = int(input())
# sang = list(map(int, input().split())) # []로 감싸면 2차원 배열 간주?
# M = int(input())
# check = list(map(int, input().split()))

# result = [0]*M
# for i in range(len(check)):
#     for j in range (len(sang)):
#         if check[i] == sang[j]:
#             result[i] = 1

# print(result)