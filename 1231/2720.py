import sys
input = sys.stdin.readline

T = int(input())
list = [25,10,5,1]
result = [[0]*4 for _ in range(T)]
for k in range(T):
    i = 0
    C = int(input())
    while C > 0:
        if C < list[i]:
            i+=1
            continue
        C = C - list[i]
        result[k][i]+=1
    for item in result[k]:
        print(item, end=" ")
    print()