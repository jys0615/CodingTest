### 오토에버 대비 암기 템플릿 ###
import heapq

def dijkstra(start, n, graph):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, curr = heapq.heappop(pq)
        
        if dist[curr] < d: continue
        
        for next_node, weight in graph[curr]:
            cost = d + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    return dist

def dijkstra(start, n, graph):
    dist = [float('inf')]*(n+1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, curr = heapq.heapppop(pq)

        if dist[curr] < d:
            continue
        for next_node, weight in graph[curr]:
            cost = d+weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    return dist