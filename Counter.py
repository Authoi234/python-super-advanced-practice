from collections import Counter

c = Counter()
c["a"] = 3
c["b"] = 5
c["d"] = 4

print(c) 
# Counter({'b': 5, 'd': 4, 'a': 3})

print(c["a"]) # 3
print(c["b"]) # 5
print(c["c"]) # 0
print(c["d"]) # 4

c = Counter(["a", "b", 'd', 'a', 'a', 'a', 'd'])
print(c) # Counter({'a': 4, 'd': 2, 'b': 1})

c = Counter({'a': 4, 'd': 2, 'b': 1})
print(c) # Counter({'a': 4, 'd': 2, 'b': 1})

c = Counter(a=4, b=1, d=2)
print(c) # Counter({'a': 4, 'd': 2, 'b': 1})

print(c.elements()) # <itertools.chain object at 0x00000246CCE12200>

print([x for x in c.elements()]) # ['a', 'a', 'a', 'a', 'b', 'd', 'd']

print(c.most_common()) # [('a', 4), ('d', 2), ('b', 1)]
print(c.most_common(1)) # [('a', 4)]
print(c.most_common(2)) # [('a', 4), ('d', 2)]

d = Counter(a=1,b=2,c=3,d=4)
c.subtract(d)

print(c) # Counter({'a': 3, 'b': -1, 'd': -2, 'c': -3})

print(c.total()) # -3 # That make sum of all the numbers of elements here, 3+(-1)+(-2)+(-3) = -3

c.clear()
print(c) # Counter()