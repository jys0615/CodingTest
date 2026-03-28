import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    row = list(map(int, input().split()))

    for num in row:
        if len(heap) < N:
            heapq.heappush(heap, num)

        else:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])      