import sys
input = sys.stdin.readline

while True:
    num = int(input())
    sum = 0
    divisor = []
    if num == -1:
        break
    for i in range(1, num):
        if num % i == 0:
            divisor.append(i)
            sum+=i
    if sum == num:
            print(f"{num} =", end="")
            for i in range(len(divisor)):
                 if i == len(divisor) - 1:
                      print(f" {divisor[i]}")
                 else:
                      print(f" {divisor[i]} +", end="")
    else:
         print(f"{num} is NOT perfect.")