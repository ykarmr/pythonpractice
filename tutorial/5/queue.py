from collections import deque
queue=deque(['Eric','John','Michael'])
queue.append('Terry')
print(queue)
print(queue.popleft())
print(queue)
print(queue.pop())
print(queue)
queue.clear()
print(queue)
