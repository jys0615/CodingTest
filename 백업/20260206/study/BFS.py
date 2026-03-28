### 그래프 탐색 - 어떤 것들이 연속으로 이어질 때, 모두 확인하는 법 ###
### 그래프 : Vertex + Edge ###
### BFS - 너비 우선 탐색 ###
### BFS는 자식의 자식을 우선으로 본다 ###

### 아이디어 ###
# 각 vertex에 연결된 vertex 찾기
# 찾은 vertex를 큐에 저장
# 큐의 가장 먼저 것을 뽑아서 반복

# 큐는 들어온 순서대로 나간다. 반대 개념은 스택.
## 시간복잡도: 알고리즘이 얼마나 올래 걸리는가?
## BFS: O(V+E)
## vertex의 개수의 edge의 개수의 합
## 연산이 어떻게? 1번 먼저 a,b 엣지를 통해서 2, 5번 vertex
## 검색할 그래프, 방문여부 확인, 큐를 이용해서 BFS를 실행한다

### 백준 1926 ###
## 1이 나올 때마다 BFS
## 2중 for문에서는 값이 1이고, 방문 안 한 곳을 간다.
## 그림 개수를 올려줘야 되고, 최댓값을 찾아줘야 한다

"""
1. 아이디어
- 2중 for문 -> 값이 1이고 방문 안 한 걸 BFS
-BFS 돌면서 그림 개수 +1, 최댓값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E = 5 * 250000 = 100만 < 2억 >> 가능!
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 여부 : bool[][]
- QUEUE(BFS)
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == 1 and chk[ny][nx] == False:
                    rs+=1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs


cnt = 0
maxv = 0

for j in range(n):
    for i in range(m):
        if arr[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 개수를 하나 늘린다
            cnt += 1
            # BFS로 그림의 크기를 구한다
            maxv = max(maxv, bfs(j, i))
            # BFS 결과를 최댓값에 갱신

print(cnt)
print(maxv)