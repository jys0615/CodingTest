"""
================================================================
CJ 코테 5개 유형 — 타이핑 암기 파일
이분탐색 / 누적합 / 슬라이딩윈도우 / 스택 / 그리디
================================================================
사용법: 주석만 보고 코드를 직접 타이핑. 막히면 아래 답 확인.
================================================================
"""


# ================================================================
# 1. 이분탐색
# ================================================================

# [패턴 1] 값 찾기
# lo, hi 설정 → mid 계산 → 조건에 따라 범위 이동

from bisect import bisect_left, bisect_right

arr = [1, 3, 5, 7, 9, 11]
target = 7

lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1


# [패턴 2] 매개변수 탐색 — "조건 만족하는 최댓값/최솟값 찾기"
# 핵심: 조건 함수 따로 만들기 → lo/hi 이동

# 예시: 나무 자르기 (BOJ 2805)
# 높이 H로 자를 때 목재 합이 M 이상인지 확인
def can_get(trees, H, M):
    return sum(max(0, t - H) for t in trees) >= M

trees = [20, 15, 10, 17]
M = 7
lo, hi = 0, max(trees)
result = 0

while lo <= hi:
    mid = (lo + hi) // 2
    if can_get(trees, mid, M):
        result = mid        # 조건 만족 → 저장 후 더 크게 시도
        lo = mid + 1
    else:
        hi = mid - 1        # 조건 불만족 → 더 작게

print(result)               # 15


# [패턴 3] bisect — 정렬 배열에서 위치 찾기
arr = [1, 3, 3, 5, 7]
print(bisect_left(arr, 3))   # 1 (같은 값 중 왼쪽)
print(bisect_right(arr, 3))  # 3 (같은 값 중 오른쪽)

# arr에 x가 존재하는지 확인
x = 3
idx = bisect_left(arr, x)
exists = idx < len(arr) and arr[idx] == x


# ================================================================
# 2. 누적합
# ================================================================

# [패턴 1] 1D 누적합 — 구간 [l, r] 합을 O(1)로
# ★ 1-indexed (크기 N+1)로 만들어야 경계 실수 없음

arr = [3, 1, 4, 1, 5, 9, 2, 6]
N = len(arr)

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

# 구간 [l, r] 합 (0-indexed)
l, r = 2, 5
result = prefix[r+1] - prefix[l]   # 4+1+5+9 = 19
print(result)


# [패턴 2] 2D 누적합 — 직사각형 구간 합을 O(1)로

N, M = 3, 3
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ps = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        ps[i][j] = board[i-1][j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

# 직사각형 (r1,c1)~(r2,c2) 합 (1-indexed)
def rect_sum(r1, c1, r2, c2):
    return ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1]

print(rect_sum(1, 1, 2, 2))    # 1+2+4+5 = 12


# [패턴 3] 합이 K인 구간 개수 — prefix + 해시맵
from collections import defaultdict

arr = [1, 2, 3, -1, 2]
K = 4
count = defaultdict(int)
count[0] = 1        # ★ 빈 구간 처리 필수
prefix = 0
result = 0

for x in arr:
    prefix += x
    result += count[prefix - K]
    count[prefix] += 1

print(result)       # 2


# ================================================================
# 3. 슬라이딩 윈도우
# ================================================================

# [패턴 1] 고정 크기 윈도우 — 최대 합
# 핵심: 새 원소 더하고, 빠진 원소 빼기

arr = [2, 1, 5, 1, 3, 2]
K = 3

window_sum = sum(arr[:K])
max_sum = window_sum

for i in range(K, len(arr)):
    window_sum += arr[i]
    window_sum -= arr[i - K]
    max_sum = max(max_sum, window_sum)

print(max_sum)      # 9


# [패턴 2] 가변 크기 윈도우 — 투 포인터
# 핵심: 조건 만족하는 동안 while로 왼쪽 수축 (if 아님!)

arr = [2, 3, 1, 2, 4, 3]
target = 7
lo, current_sum = 0, 0
min_len = float('inf')

for hi in range(len(arr)):
    current_sum += arr[hi]
    while current_sum >= target:        # ★ while (if 아님)
        min_len = min(min_len, hi - lo + 1)
        current_sum -= arr[lo]
        lo += 1

print(min_len)      # 2 ([4, 3])


# [패턴 3] 윈도우 내 최솟값 — 단조 deque
from collections import deque

arr = [1, 3, -1, -3, 5, 3, 6, 7]
K = 3
result = []
dq = deque()        # 인덱스 저장, 단조 증가 유지

for i in range(len(arr)):
    if dq and dq[0] < i - K + 1:       # 윈도우 밖 제거
        dq.popleft()
    while dq and arr[dq[-1]] >= arr[i]: # 현재보다 크면 제거
        dq.pop()
    dq.append(i)
    if i >= K - 1:
        result.append(arr[dq[0]])       # 앞이 항상 최솟값

print(result)       # [-1,-3,-3,-3,3,3]


# ================================================================
# 4. 스택
# ================================================================

# [패턴 1] 괄호 검사

def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_valid("({[]})"))   # True
print(is_valid("({[})"))    # False


# [패턴 2] 단조 스택 — 오른쪽으로 첫 번째 큰 수 찾기
# ★ 스택에 값이 아닌 인덱스를 저장

arr = [2, 1, 5, 3, 6, 4]
result = [-1] * len(arr)
stack = []

for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        result[idx] = arr[i]
    stack.append(i)

print(result)       # [5, 5, 6, 6, -1, -1]


# [패턴 3] 괄호 카운터 — 스택 없이 O(1) 공간

def check(s):
    cnt = 0
    for ch in s:
        if ch == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:     # 닫는 괄호가 더 많으면 즉시 False
                return False
    return cnt == 0         # 열린 괄호 남으면 False

print(check("(())()"))  # True
print(check(")("))      # False


# [패턴 4] 스택 + 그리디 — 큰 수 만들기 (BOJ 16675 계열)
# K개 제거해서 가장 큰 수

N = "1924"
K = 2
stack = []

for digit in N:
    while K > 0 and stack and stack[-1] < digit:
        stack.pop()
        K -= 1
    stack.append(digit)

result = "".join(stack[:-K] if K else stack)
print(result)       # "94"


# ================================================================
# 5. 그리디
# ================================================================

# [패턴 1] 회의실 배정 — 끝 시간 기준 정렬
# ★ 왜 끝 시간 기준? → 일찍 끝나야 다음 회의 여유가 생김

meetings = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11)]
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)        # 4


# [패턴 2] 거스름돈 — 큰 단위부터 최대한
# 단, 동전이 배수 관계일 때만 성립. 임의 값이면 DP 필요.

coins = [500, 100, 50, 10]
amount = 1260
count = 0

for coin in coins:
    count += amount // coin
    amount %= coin

print(count)        # 6


# [패턴 3] 구간 합 최대 (카데인 알고리즘)
# 연속 부분 배열의 최대 합

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = arr[0]
current = arr[0]

for x in arr[1:]:
    current = max(x, current + x)   # 새로 시작 vs 이어가기
    max_sum = max(max_sum, current)

print(max_sum)      # 6 ([4,-1,2,1])


# ================================================================
# 핵심 실수 모음 — 이것만 기억해도 절반은 맞음
# ================================================================
"""
이분탐색:
    lo <= hi 로 시작 (< 아님)
    매개변수 탐색: 조건 만족하면 result 저장 후 lo = mid + 1

누적합:
    prefix 크기 N+1, 1-indexed
    구간 [l, r] = prefix[r+1] - prefix[l]
    합이 K인 구간: count[0] = 1 초기화 필수

슬라이딩 윈도우:
    가변 크기: while (if 아님) 로 수축
    단조 deque: 값 아닌 인덱스 저장

스택:
    단조 스택: 인덱스 저장
    괄호: stack이 비었을 때 pop 시도하면 런타임 에러

그리디:
    회의실: 끝 시간 기준 정렬 (시작 시간 아님)
    거스름돈: 동전이 배수 관계일 때만 그리디 가능
"""
