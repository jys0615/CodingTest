from collections import deque

queue = deque() # deque()로 큐 구현을 한다.
# 리스트를 이용해서 pop을 사용하면 원소 위치 조정 과정이 필요해서
# 5^K 만큼의 시간복잡도가 필요함. deque이 더 빠르다.

queue.append(5) # 오른쪽으로 들어와서 
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 왼쪽으로 나간다
queue.append(1) 
queue.append(4) # 삽입
queue.popleft() # 삭제

print(queue)
queue.reverse() # 역순으로 바꾸기
print(queue) 