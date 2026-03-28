import sys
input = sys.stdin.readline

count = [0]*26

word = input().rstrip() # 개행 제거

for w in word:
    if ord(w) >= 97: # 소문자 처리
        count[ord(w)-97] += 1
    else: # 대문자 처리
        count[ord(w)-65] += 1
        
max_count=0 # 최대 카운트에 해당하는 알파벳 개수
for item in count:
    if item == max(count):
        max_count += 1
        
if max_count > 1: # 알파벳 개수가 2개 이상이면 ?
    print('?')
else: # 1개면 해당 알파벳 출력
    print(chr(count.index(max(count))+65))