### SET ###
# 중복을 허용하지 않음
# 순서가 없어서 인덱스 접근 불가능
# 해시를 사용해서 매우 빠르다
# s = {1, 2, 3}
# 존재 확인 여부에 사용
# add, remove(없으면 에러)/discard(없어도 에러 없음)
# if x in s:
# A.intersection(B)
# A | B
# A - B
# A ^ B -> 대칭 차집합. 서로 겹치지 않는 것만

import sys
input = sys.stdin.readline

### 출력 초과 방지 답안 ###
N, M = map(int, input().split())

S = set()
for _ in range(N):
    S.add(input().rstrip())

str1 = []
for _ in range(M):
    str1.append(input().rstrip())

count = 0
for i in range(M):
    if str1[i] in S: ### 해시는 in 연산이 O(1)
        count += 1

print(count)

### str1은 set을 하면 안 됨. 이럼 중복이 없어짐 ###
# N, M = map(int, input().split())

# S = set()
# for _ in range(N):
#     S.add(input().rstrip())

# str1 = set()
# for _ in range(M):
#     str1.add(input().rstrip())

# count = len(str1.intersection(S))

# print(count)

### 출력 초과 ###

# N, M = map(int, input().split())

# S = []
# for _ in range(N):
#     S.append(input().rstrip())
# str1 = []
# for _ in range(M):
#     str1.append(input().rstrip())

# count = 0
# for i in range(M):
#     if str1[i] in S: ### 초과 발생 원인.
#         count+=1
# print(count)