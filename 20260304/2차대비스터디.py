### Unit 0 — Python 코테 필수 도구 암기 ###

## ✅ collections.deque — BFS의 심장 ##
from collections import deque
q = deque()
q.append(1) # 오른쪽 추가
q.appendleft(1) # 왼쪽 추가
q.pop() # 오른쪽 제거
q.popleft() # 왼쪽 제거 <- BFS에서 이것만 쓴다

## ✅ heapq — 최소 힙 (우선순위 큐) ##
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

heapq.heappop(heap)

# ⚠️ Python heapq는 최소 힙만 지원
# 최대 힙이 필요하면? → 값에 -1 곱해서 넣고 꺼낼 때 -1 곱하기
heapq.heappush(heap, -5)
-heapq.heappop(heap) # 5

# 다익스트라, 그리드 등에서 핵심 사용
# (거리, 노드) 튜플로 쓰는 패턴 기억
dist, node = heapq.heappop(heap)
heapq.heappush(heap, (dist, node))

## ✅ bisect — 이진탐색 라이브러리 ##
from bisect import bisect_left, bisect_right

arr = [1,2,4,4,5,7]

bisect_left(arr, 4) # 2 → 4가 들어갈 가장 왼쪽 인덱스
bisect_right(arr, 4) # 4 → 4가 들어갈 가장 오른쪽 인덱스

# 활용: arr에서 4의 개수
count = bisect_right(arr, 4) - bisect_left(arr, 4) # 2

# 활용: x 이상인 첫 번째 값의 인덱스
idx = bisect_left(arr, x)

## ✅ 자주 쓰는 Python 문법 패턴 ##
# 무한대
INF = float('inf')

graph = [[0] * m for _ in range(n)]

# 입력 빠르게 받기
import sys
input = sys.stdin.readline

# 딕셔너리 기본값
from collections import defaultdict
d = defaultdict(int)
d = defaultdict(list)

# Counter
from collections import Counter
c = Counter([1,1,2,3,3,3])
c.most_common(1) # [(3, 3)]

### Unit 1 — BFS/DFS ###

## BFS 완성 템플릿 ##
from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start]= True

    while q:
        v = q.popleft()
        print(v)

        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

## 2차원 그리드 BFS (소마 빈출 패턴) ##
from collections import deque

def bfs_grid(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    dist = 0

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    while q:
        dist+=1
        for _ in range(len(q)):
            r, c = q.popleft()
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return dist

## DFS 두 가지 방식 ##
# 재귀 방식 (코드 간결, 스택 깊이 주의)
import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    visited[v] = True
    for nxt in graph[v]:
        dfs(graph, nxt, visited)

def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for nxt in graph[v]:
                if nxt not in visited:
                    stack.append(nxt)

# 💡 언제 BFS? 언제 DFS?
    # 최단 거리/경로 → BFS
    # 가능한 경우 탐색, 연결 요소 개수 → DFS
    # 그래프 사이클 판별 → DFS

### Unit 2 — DP ###

## 패턴 1: 1D DP - 배낭/계단 유형 ##
# 계단 오르기 유형 (연속 3칸 못 밟는 조건)
# dp[i] = i번 계단까지 올라올 때 최대 점수
n = int(input())
stair = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]

for i in range(3, n+1):
    # i번 밟는 경우:
    # 1) (i-2)번 밟고 i번 밟기
    # 2) (i-3)번 밟고 (i-1)번 밟고 i번 밟기
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

## 패턴 2: 2D DP — 경로/LCS 유형 ##
# 최소 비용 경로 (오른쪽/아래로만 이동)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')] * m for _ in range(n)]

dp[0][0] = grid[0][0]

for i in range(n):
    for j in range(m):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])

## 패턴 3: DP + 힙 (소마 16기 4번 유형) ##
# 두 개의 우선순위 큐를 이용한 DP 패턴
# "k번째로 작은 합" 류의 문제
import heapq

# 핵심 아이디어: dp[i] = i번째 최솟값
# heap에서 꺼내면서 상태 전이
heap = [(초기값, 상태)]
visited = set()

while heap:
    cost, state = heapq.heappop(heap)
    if state in visited:
        continue
    visited.add(state)

    # 다음 상태 전이
    for next_state in get_next(state):
        heapq.heappush(heap, (cost + ..., next_state))

# 💡 DP 문제 접근 순서
    # dp[i]의 의미를 명확히 정의
    # 점화식 세우기 (i를 구하기 위해 이전 무엇이 필요?)
    # 초기값(base case) 설정
    # 순서 결정 (작은 것부터? 큰 것부터?)

### Unit 3 — 이진탐색 ###

## 기본 구현 (외워야 함) ##
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

## 실전 패턴: 매개변수 탐색 (Parametric Search) ##
# 소마 2차에서 이진탐색이 나오면 거의 이 형태
# "최솟값의 최댓값" 또는 "최댓값의 최솟값" 을 구하는 문제.
def can_do(mid, ...):
    # mid가 정답이 될 수 있는지 검증하는 함수
    # True/False 반환
    pass

left, right = 최솟값, 최댓값
answer = 0

while left <= right:
    mid = (left + right) // 2

    if can_do(mid):
        answer = mid
        left = mid + 1
        # right = mid - 1
    else:
        right = mid - 1
        # left = mid + 1

print(answer)

### Unit 4 — 구현/시뮬레이션 (소마 1번 유형) ###
## 가장 중요해. 16기 1번이 구현+그리디, 2번이 구현+해시였어. 

## 구현 문제 접근 공식
"""
    1. 문제를 읽으며 "상태"가 무엇인지 파악
    2. "상태 전이 조건"을 if문으로 표현
    3. 반복/시뮬레이션 구조 잡기
    4. 엣지케이스: 경계값, 빈 입력, 최대/최솟값
"""

## 그리디 판별법
"""
"매 순간 최선의 선택이 전체 최선"이 성립하는지 먼저 증명
→ 성립하면 그리디, 안 되면 DP

소마 그리디 빈출:
- 정렬 후 순서대로 처리
- 우선순위 큐(heapq)로 최솟값/최댓값 유지
- 구간 합 (prefix sum)
"""

from collections import defaultdict, Counter
# 패턴 1: 빈도 카운팅
freq = Counter(arr)

# 패턴 2: 그룹핑
groups = defaultdict(list)
for item in data:
    key = get_key(item)
    groups[key].append(item)

lookup = {val: idx for idx, val in enumerate(arr1)}
for val in arr2:
    if val in lookup:
        ...

"""
[ BFS ]
- deque + popleft
- visited는 append할 때 처리
- 최단거리 = BFS 레이어 수

[ DFS ]
- sys.setrecursionlimit(10**6) 필수
- 재귀 or 스택

[ DP ]
- dp[i]의 의미 먼저 정의
- base case 확인
- 점화식 → 코드

[ 이진탐색 ]
- while left <= right
- mid = (left + right) // 2
- 매개변수 탐색: can_do() 함수 분리

[ 힙 ]
- heappush / heappop
- 최대힙은 -1 곱하기
- (비용, 노드) 튜플 패턴

[ 구현 ]
- 2차원 배열: [[0]*m for _ in range(n)]
- INF = float('inf')
- 입력 빠르게: sys.stdin.readline
"""