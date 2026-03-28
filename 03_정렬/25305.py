import sys
input = sys.stdin.readline

N, k = map(int, input().split())
arr = list(map(int, input().split())) # 리스트로 감싸야 sort 가능. 

arr.sort(reverse=True)
print(arr[k-1])