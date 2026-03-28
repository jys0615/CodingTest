import sys
input = sys.stdin.readline

p, q = map(int, input().split())

divisor = []

for i in range(1, p+1):
    if p % i == 0:
        divisor.append(i)
        
if q > len(divisor):
    print(0)
else:
    print(divisor[q-1])
