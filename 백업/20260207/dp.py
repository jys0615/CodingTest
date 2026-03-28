### Dynamic Programming ###
## 이전의 값을 재활용하는 알고리즘 
## 1~10 숫자 중, 각각 이전 값들을 합한 값 구하기
## 이전의 값을 활용해서 시간복잡도 줄일 수 있음

## DP는 점화식이 중요. 그려서라도 규칙을 찾아라 ##
## 점화식을 명확하게 세우고 코드를 짠다 ##
import sys
input = sys.stdin.readline

n = int(input())
rs = [0,1,2]

for i in range(3, n+1):
    rs.append((rs[i-1] + rs[i-2])%100007)

print(rs[n])

