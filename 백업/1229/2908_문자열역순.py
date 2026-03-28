import sys
input = sys.stdin.readline

A, B = list(input().split())
reverse_A = ''
for c in A:
    reverse_A = c + reverse_A
reverse_B = ''
for c in B:
    reverse_B = c + reverse_B
print(max(int(reverse_A),int(reverse_B)))

### 이 방식으로는 문자열 역순 불가 ###
# i = 0
# j = len(A)-1
# while i < j:
#     A[i], A[j] = A[j], A[i]
#     i+=1
#     j-=1

# i = 0
# j = len(B)-1
# while i < j:
#     B[i], B[j] = B[j], B[i]
#     i+=1
#     j-=1

# print(A, B)

