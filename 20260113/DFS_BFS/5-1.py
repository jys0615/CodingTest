stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력. 처음:끝:스텝,,스텝 -1이면 뒤에서부터 앞으로 1칸씩 이동.
print(stack) # 최하단 원소부터 출력 