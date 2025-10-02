from collections import deque

d = deque()

print(d) # deque([])

d.extend([1,2,3,4,5,6,7])
print(d) # deque([1, 2, 3, 4, 5, 6, 7])

d.append(8)
print(d) # deque([1, 2, 3, 4, 5, 6, 7, 8])

print(d.pop()) # 8

print(d.popleft()) # 1

d.appendleft(1)
print(d) # deque([1, 2, 3, 4, 5, 6, 7])

d = deque(maxlen=3)

d.append(1)
d.append(2)
d.append(3)
print(d) # deque([1, 2, 3], maxlen=3)
d.append(4)
print(d) # deque([2, 3, 4], maxlen=3)
d.appendleft(5)
print(d) # deque([5, 2, 3], maxlen=3)

d = deque([1,2,3], maxlen=5)
print(d) # deque([1, 2, 3], maxlen=5)

d = deque("abcd", maxlen=3)
print(d) # deque(['b', 'c', 'd'], maxlen=3)