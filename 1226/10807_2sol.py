### 모범답안 ###
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))

### 내가 쓴 답안 ###
# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = map(int, input().split())
# v = int(input())
# count = 0
# for val in arr:
#     if val == v:
#         count+=1

# print(count)
