import sys
input = sys.stdin.readline

print(input().strip() + "??!")

## input = sys.stdin.readline은 줄바꿈을 포함해서 반환. 따라서, 이걸 유지한다면 
## Strip()을 사용해야 한다.