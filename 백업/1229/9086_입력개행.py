# import sys
# input = sys.stdin.readline # 입력 문자열 끝에 \n 포함

# T = int(input())

# for _ in range(T):
#     str1 = input()
#     print(str1[0]+str1[len(str1)-1])

### 다른방법 ###
import sys
input = sys.stdin.readline # 입력 문자열 끝에 \n 포함

T = int(input())

for _ in range(T):
    str1 = input().rstrip() # 오른쪽(개행)만 제거
    print(str1[0]+str1[len(str1)-1])


# strip() vs rstrip()
# 	strip() : 양쪽 공백 제거
# 	rstrip() : 오른쪽(개행)만 제거