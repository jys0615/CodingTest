### 간선: 어디부터 어디까지 연결
## 1. 인접 배열 2. 인접 리스트 -> 다익스트라는 리스트
## 힙 시작점 추가: 1에서 한다면 힙에 시작점을 넣는다.
## 거리 배열을 처음에는 무한대로 설정
## 힙에서 현재 노드 빼면서 간선을 통할 때 더 거리가 짧아진다.
## 간선을 통할 때 더 거리가 짧아진다면 거리 갱신 및 힙에 추가
## 만약 갈 수 있는 경로가 없다면 그대로 INF 유지한다.

### CODE ###
# dist[k] = 0
# heapq.heappush(heap, (0, k))

# while heap:
#     w, v = heapq.heappop(heap)
#     if w != dist[v]: continue
#     for nw, nv in edge[v]:
#         if dist[nv] > dist[v] + nw:
#             dist[nv] = dist[v] + nw
#             heapq.heappush(heap, (dist[nv], nv))

##### 백준 1753 - 최단경로 #####
### 아이디어 ###
# 한 점에서 다른 모든 점으로의 최단경로 > 다익스트라 사용
# 모든 점 거리 초기값 무한대로 설정
# 시작점 거리 0 설정 및 힙에 추가
# 힙에서 하나씩 빼면서 수행할 것
    # 현재 거리가 새로운 간선 거칠 때보다 크다면 갱신
    # 새로운 거리를 힙에 추가
# 시간복잡도 : ElgV
    # E: 3e5, lgV = 20
# O(ElgV) = 6e6 > 가능

# 변수
    # 다익스트라 사용 힙: (비용(int), 다음 노드(int))[]
        # 비용 최댓값: 10*2e4 = 2e5 => INT 가능
        # 다음 노드: 2e4 => INT 가능
    # 거리 배열: int[]
        # 거리 최댓값: 10*2e4 = 2e5 => INT 가능
    # 간선, 인접 리스트: (비용(int), 다음 노드(int))[]

"""
1. 아이디어
- 한 점 시작해서 모든 거리 : 다익스트라
- 간선, 인접 리스트 저장
- 거리 배열 무한대 초기화
- 시작점 : 거리배열 0, 힙에 넣어주기
- 힙에서 빼면서 다음의 것들 수행
    - 최신값인지 먼저 확인
    - 간선을 타고 간 비용이 더 작으면 갱신

2. 시간복잡도
- 다익스트라 : O(ElgV)
    - E : 3e5
    - V : 2e4
    - ElgV = 6e6 > 가능

3. 변수
- 힙 : (비용, 노드번호)
- 거리 배열 : 비용 : int[]
- 간선 저장, 인접리스트 : (비용, 노드번호)[]
"""
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())
edge = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for i in range(E):
    u,v,w = map(int, input().split()) 
    # u->v로 가는 길이 있고 그 비용이 w
    edge[u].append([w,v])

dist[K] = 0
heap = [[0,K]]

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: # dist[ev]는 최신값, ew는 오래된 값
        continue
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])

for i in range(1, V+1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])