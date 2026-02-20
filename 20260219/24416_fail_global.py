import sys
input = sys.stdin.readline

N = int(input())

def fib(n, count):
    if n == 1 or n == 2:
          return 1 # 코드1
    else:
        return (fib(n - 1) + fib(n - 2));


def fibonacci(n, count):
    count = 0
    fibonacci(1) = 1
    fibonacci(2) = 1
    for i in range(3, n):
        count += 1
        fibonacci(i) = fibonacci(i-1) + fibonacci(i-2)
    return fibonacci(n);

print(fib(N, 0))
print(fibonacci(N, 0))
