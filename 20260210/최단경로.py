### 가장 짧은 경로를 찾는 알고리즘
## 한 지점에서 다른 한 지점까지의 최단
## 한 지점에서 다른 모든 지점까지의 최단 경로
## 모든 지점에서 다른 모든 지점까지의 최단 경로
## 각 지점은 그래프에서 노드로 표현

### 1. 다익스트라 알고리즘 ###
# 특정 노드에서 다른 모든 노드로 가는 최단 경로
# 음의 간선이 없을 때 동작 가능
# 그리디 알고리즘 - 매 상황에서 비용이 적은 노드를 선택.

'''
알고리즘의 동작 과정
    1. 출발 노드를 설정
    2. 최단 거리 테이블을 초기화
    3. 방문 안 한 노드 중에서 최단 거리가 가장 짧은 노드를 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산 -> 최단 거리 테이블을 갱신
    5. 위 과정에서 3번, 4번을 반복한다.
'''

### 처리하는 과정에서 더 짧은 경로를 찾으면 갱신한다 ###
### 테이블은 초기에 무한대로 초기화한다 ###
### 방문 안 한 노드 중에서 최단 거리가 가장 짧은 노드인 1번을 선택한다 ###
### 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택 ###
### 기존 거리와 비교해서 짧은 게 아니면 테이블 갱신을 안 한다. ###

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index



