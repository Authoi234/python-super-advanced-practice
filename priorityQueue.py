from queue import PriorityQueue

pq= PriorityQueue()
pq.put((3,"write code"))
pq.put((2,"write tests"))
pq.put((1,"create specification"))
pq.put((4,"release product"))

print(pq.get()) # (1, (1, 'create specification')
print(pq.get()) # (1, (2, 'write tests')
print(pq.get()) # (1, (3, 'write code')
print(pq.get()) # (1, (4, 'release product')