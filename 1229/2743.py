import sys
input = sys.stdin.readline

str1 = input()
print(len(str1)-1) # 상단에 입력 설정 해두면 본래 문자 길이+1이여서 -1을 해야 한다.

### 모범답안
# print(len(input()))