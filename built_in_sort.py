from operator import itemgetter

def compare_fnc(item):
    return item[1]

fruits = [('banana', 2), ('guava', 5), ('date', 4), ("orange", 3), ("mango", 1), ('apple', 3)]

# sort by quantity
print(sorted(fruits, key=lambda x: x[1]))

print(sorted(fruits, key=compare_fnc))

print(sorted(fruits, key=itemgetter(1)))

# reversed sort by quantity
print(sorted(fruits, key=itemgetter(1), reverse=True))

# sort by quantity (priority first) and name
print(sorted(fruits, key=itemgetter(1, 0)))

print(sorted(sorted(fruits, key=itemgetter(0)), key=itemgetter(1)))