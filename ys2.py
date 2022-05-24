from collections import deque

Q = deque()
Q.append((5, 3))

while Q:
  y, x = Q.popleft
  print(y, x)
