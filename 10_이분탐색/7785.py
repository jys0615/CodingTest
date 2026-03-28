import sys
input = sys.stdin.readline

N = int(input())
emp_list = []
for _ in range(N):
    emp, check = input().split()
    if check == 'enter':
        emp_list.append(emp)
    else:
        emp_list.remove(emp)
emp_list.sort(reverse=True)
for emp in emp_list:
    print(emp)