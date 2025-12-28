import sys
input = sys.stdin.readline

N,M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(M)]
count = [0]*N
for i in range(M): 
    for data in range (map[i][0], map[i][1]+1):
        # 그냥 in이라고 하면 해당 숫자들만 바뀜
        count[data-1] = map[i][2]

for num in count: # 그냥 count 출력시키면 배열 형태로 결과 불일치
    print(num, end=" ") # 띄어쓰기 기준, 줄바꿈 X