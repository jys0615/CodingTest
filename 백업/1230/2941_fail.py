import sys
input = sys.stdin.readline

word = input().rstrip()
count = 0

check = ["c=", "c-", "dz=", "d-", "lj", "nj",
         "s=", "z="]

### 정답 코드 - 너무 간단. 그냥 해당 문자를 1개의 문자로 변환
for ch in check:
    word = word.replace(ch, "^")
print(len(word))


### 내 방식은 공백 기준으로 문제를 푸는 것이나, 매우 복잡
## 그리고 유사한 패턴들에 대해서 오류 발생 빈번히 일어나는 오답 코드
# for ch in check:
#     if ch in word:
#         m = len(word)
#         new_word = word.replace(ch, " ")
#         n = len(word.replace(" ", ""))
#         print(m, n)
#         count+=1*((m-n) // len(ch))
#         word =

# count += len(word.replace(" ", ""))
# print(count)