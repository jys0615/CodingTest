import heapq

heap = []

heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)

print(heap) # [1, 2, 3]
print(heapq.heappop(heap)) # 1
print(heapq.heappop(heap)) # 2
print(heapq.heappop(heap)) # 3

heapq.heappush(heap, (5, 'A'))
heapq.heappush(heap, (1, 'B'))
print(heap) # [(1, 'B'), (5, 'A')]
print(heapq.heappop(heap)) # (1, 'B')

##### 다익스트라 #####

import heapq

def dijkstra(graph, start):
    INF = float('inf')
    dist = [INF] * (len(graph)+1)
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)

        if cost > dist[node]:
            continue

        for next_node, weight in graph[node]:
            new_cost = cost + weight
            if dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

        return dist

# 그래프 예시: 인접 리스트 형태
graph = {
    1: [(2, 2), (3, 5)],
    2: [(3, 1)],
    3: []
}

print(dijkstra(graph, 1))  # [INF, 0, 2, 3]