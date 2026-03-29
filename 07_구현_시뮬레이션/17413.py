import sys
input = sys.stdin.readline

S = input().rstrip()
i = 0

while i < len(S):
    if S[i] == '<':
        tag = ''
        while S[i] != '>':
            tag+=S[i]
            i+=1
        tag+='>'
        i+=1
        print(tag, end="")
    elif S[i] == ' ':
        print(S[i], end="")
        i+=1
    else:
        word = ''
        while i < len(S) and S[i] != ' ' and S[i] != '<':
            word += S[i]
            i+=1
        print(word[::-1], end="") # 역순으로 출력하는 법