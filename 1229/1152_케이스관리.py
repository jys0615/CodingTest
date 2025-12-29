import sys
input = sys.stdin.readline

str1 = input().strip()
if len(str1) == 0:
    print(0)
else:
    count = 1
    for str in str1:
        if str == " ":
            count+=1
    print(count)


### 틀린 이유: 공백 개수 = 단어 개수가 아님.
## 
# import sys
# input = sys.stdin.readline

# str1 = input().strip()
# count=1
# for str in str1:
#     if str == " ":
#         count+=1
# print(count)