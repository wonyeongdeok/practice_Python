'''큐 is 선입선출'''
'''나중에 들어온 사람일수록 나중에 들어가기 때문에 흔히 '공정한 자료구조'라고 비유'''

# 큐(Queue) 구현을 ㅟ해 deque 라이브러리 사용
from collections import deque


queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

type(queue)
list(queue)
