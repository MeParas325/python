# Map
l1 = [1, 2, 3, 4]

def map_func(item):
    return item * item
    
newList1 = list(map(map_func, l1))
print(newList1)


# Filter
l2 = [1, 2, 3, 4]

def filter_func(item):
    return item % 2 == 0
    
newList2 = list(filter(filter_func, l2))
print(newList2)

from functools import reduce
# Reduce
l3 = [1, 2, 3, 4]
    
newList3 = reduce(lambda x, y: x + y, l3)
print(newList3)


