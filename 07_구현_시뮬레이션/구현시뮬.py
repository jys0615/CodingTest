"""
전체 지도 : int[][]
내 위치, 방향 : int, int, int (y, x, d)

0 : 청소 X, 1 : 벽, 2 : 청소 O
"""

"""
1. 아이디어
- while문으로 특정 종료될 때까지 반복
- 방향을 for문으로 탐색
- 탐색 불가능할 경우, 뒤로 한 칸 후진
- 후진이 불가능하면 종료

2. 시간복잡도
- O(NM) : 50^2 = 2500 < 2억
- 가능

3. 자료구조
- map : int[][]
- 로봇청소기 위치, 방향, 전체 청소한 곳 수
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())  # 시작 위치(r,c), 방향(d)
room = [list(map(int, input().split())) for _ in range(N)]

# "방향: 0북 1동 2남 3서"
# 북쪽부터 시계방향 순서로 정의
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

count = 0  # 청소한 칸 수

while True:

    # ① "현재 위치가 청소되지 않은 경우 청소한다"
    if room[r][c] == 0:
        room[r][c] = 2   # 2 = 청소 완료 표시
        count += 1

    # ② "왼쪽 방향부터 탐색 시작"
    # 4방향을 전부 탐색해서 청소 안 된 칸이 있는지 확인
    turned = 0  # 몇 번 회전했는지
    moved = False

    for _ in range(4):
        # "왼쪽으로 회전" = 반시계방향 = (d + 3) % 4
        d = (d + 3) % 4
        ny = r + dy[d]
        nx = c + dx[d]

        # "청소되지 않은 공간이 있으면 전진"
        if 0 <= ny < N and 0 <= nx < M and room[ny][nx] == 0:
            r, c = ny, nx   # 전진!
            moved = True
            break

    # ③ "4방향 모두 청소됐거나 벽이면 → 후진"
    if not moved:
        # 현재 방향의 반대 = 후진 방향
        # "방향을 유지한 채로 한 칸 후진"
        # 후진 = 현재 보는 방향의 반대쪽
        back_y = r - dy[d]
        back_x = c - dx[d]

        # "후진할 곳이 벽이면 종료"
        if room[back_y][back_x] == 1:  # 1 = 벽
            break

        # 벽이 아니면 후진 (방향은 그대로!)
        r, c = back_y, back_x

print(count)
