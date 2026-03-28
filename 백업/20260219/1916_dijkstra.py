import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
edge = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

for i in range(M):
    u,v,w = map(int, input().split())
    edge[u].append([w,v])

start, end = map(int, input().split())

dist[start] = 0
heap = [[0,start]]

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    if ev == end:
        break
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew+nw
            heapq.heappush(heap, [dist[nv], nv])
        
print(dist[end])