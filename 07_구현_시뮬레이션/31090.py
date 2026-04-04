import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = input().strip()
    if (int(N)+1) % (int(N[2]+N[3])) == 0:
        print("Good")
    else:
        print("Bye")