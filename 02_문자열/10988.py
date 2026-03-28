import sys
input = sys.stdin.readline

word = input().rstrip()

i = 0
j = len(word)-1
answer = 1
while i < j:
    if word[i] != word[j]:
        answer = 0
    i+=1
    j-=1
print(answer)