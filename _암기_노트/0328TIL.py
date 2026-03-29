import sys
input = sys.stdin.readline
'''
2178 미로탐색 ✅
핵심: arr[ny][nx] += arr[ey][ex] 로 거리 누적 + 방문 체크 동시 처리
실수 포인트: visited 처리는 넣을 때 해야 중복 삽입 방지

14503 로봇청소기 해설 보고 이해
핵심 세 가지

(dr+3)%4 = 왼쪽 회전 공식
for-else = break 없이 끝났을 때만 else 실행 → 후진
후진 공식 ci-di[dr]


14499 주사위 굴리기 ✅
핵심: 방향별 면 회전 공식 (동: n1,n3,n4,n6 = n4,n1,n6,n3)
실수 포인트: dy 배열 중복 체크 필수, 범위 밖 명령 처리 블록 위치

14502 연구소 ✅
핵심: 브루트포스(삼중 for) + BFS 조합
실수 포인트: deepcopy vs 세웠다 허무는 방식 — arr 직접 안 건드리면 deepcopy 불필요

17413 단어 뒤집기 2 힌트 받고 완성
핵심: i를 직접 올리는 while 구조
실수 포인트: 안쪽 while에도 i < len(S) 범위 체크 따로 필요, 공백 처리 후 i+=1 누락

7562 나이트의 이동 ✅
핵심: dist 배열로 방문 체크 + 거리 추적 통일
실수 포인트: dy 배열 중복, end 조건 -1 오류, 시작=도착 엣지케이스
'''

### 0-1 BFS ###
"""
비용이 0 또는 1인 경우에만 쓸 수 있는 최단경로 알고리즘
시간복잡도는 BFS처럼 O(V+E)

일반 BFS는 큐에서 꺼낸 순서가 곧 최단거리 순서. 모든 비용이 1이면 먼저 꺼낸 게 항상 더 짧은 경로.
비용이 섞이면 전제가 깨짐. 비용 1짜리 경로로 먼저 큐에 들어갔다가, 나중에 비용 0짜리 경로가 더 짧은
거리로 도달하는 경우가 생기기 때문이다. 

핵심 구조 - 덱(deque)
    비용이 0인 경로로 이동하면 → 덱의 앞(appendleft) 에 삽입
    비용이 1인 경로로 이동하면 → 덱의 뒤(append) 에 삽입

꺼낼 때는 항상 popleft

이러한 규칙으로 "비용이 적은 게 항상 앞에 있다"는 BFS의 전제를 비용이 섞인 상황에서도 유지
"""
### 코드 ###
from collections import deque

def zero_one_bfs(graph, start, n):
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0
    dq = deque([start])

    while dq:
        cur = dq.popleft()
        for next_node, cost in graph[cur]:
            new_dist = dist[cur] + cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                if cost == 0:
                    dq.appendleft(next_node)
                else:
                    dq.append(next_node)
    return dist