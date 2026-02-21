"""
- 모든 경우의수를 확인해야 하라 때
    - for로는 확인 불가한 경우(깊이가 달라질 때)
"""

### 백준 15649 ###
'''
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문여부 확인)
- 재귀함수 M개를 선택할 경우 print

2. 시간복잡도
- 중복이 가능하면 N^N
- 중복이 불가능하면 N!

3. 자료구조
- 방문 여부 확인 배열 : bool[]
- 선택한 값 입력 배열 : int[]
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False # 이 부분이 중요. 만약 1,2인 상황이면 그 다음은 1,3인데 이 줄과 아래 줄이 없으면 1,2,3이 되어 버린다. 따라서, 지우는 백트래킹 작업이 필요
            rs.pop()

recur(0)