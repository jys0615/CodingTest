import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    item = input().rstrip()
    arr.append(item)


count = N
for word in arr:
    record = []
    for i in range(len(word)):
        if len(record) == 0:
            record.append(word[i])
            continue
        if record[-1] != word[i]:
            if word[i] not in record:
                record.append(word[i])
            else:
                count-=1
                break

print(count)