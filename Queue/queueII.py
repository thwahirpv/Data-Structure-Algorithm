from collections import deque

queue = deque()
queue.append(10)
queue.append(100)
queue.append(1000)
queue.append(10000)
print(queue[0])
queue.popleft()
print(queue)
print(queue[0])