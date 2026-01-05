import sys
input = sys.stdin.readline

N, M = map(int, input().split())

unheard = set()
for _ in range(N):
    unheard.add(input().rstrip())

unseen = set()
for _ in range(M):
    unseen.add(input().rstrip())

result = sorted(unheard.intersection(unseen))
print(len(result))
for name in result:
    print(name)