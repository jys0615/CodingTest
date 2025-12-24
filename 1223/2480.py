import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())
sum = 0
if A == B == C:
    sum = 10000+A*1000
elif A == B:
    sum = 1000+A*100
elif B == C:
    sum = 1000+B*100
elif A == C:
    sum = 1000+A*100
else:
    sum = max(A,B,C)*100
print(sum)