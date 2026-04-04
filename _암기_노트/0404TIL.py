### 다익스트라 알고리즘 ###
import heapq

def dijkstra(start, graph, n):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)

        if distances[node] < dist:
            continue

        for next, weight in graph[node]