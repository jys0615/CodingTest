### 그리디 알고리즘 ###
## 때로는 당장 눈 앞의 최선이 최고의 결과를 가져온다 ##

### Tip ###
## 그리디를 사용 하는 이유를 설명하고, 반례를 찾는 연습 
### 백준 11047 ###
## 금액을 만드는 동전의 최소 개수 ##
"""
1. 아이디어
- 동전을 오름차순으로 정렬
- 동전을 for > 
    - 동전 사용개수 추가
    - 동전 사용한 만큼 K값 갱신

2. 시간복잡도
- O(N)
3. 자료구조
- 동전 금액 : int[]
- 동전 사용 cnt : int
- 남은 금액 : int
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
cnt = 0

for each_coin in coins:
    cnt = K // each_coin
    K = K % each_coin

print(cnt)