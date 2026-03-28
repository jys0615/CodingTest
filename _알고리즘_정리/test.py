import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
edge = [[] for _ in range(m+1)]
dist = [INF]*(m+1)
for i in range(m):
    u,v,w = map(int, input().split())
    edge[u].append([w,v])
start, end = map(int, input().split())
dist[start] = 0
heap = [[0, start]]

count = 0
while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew:
        continue
    for nw, nv in edge[ev]:
        if dist[nv] > ew+nw:
            dist[nv] = ew+nw
            heapq.heappush(heap, [dist[nv], nv])

print(dist[end])
print(heap)