# How to create a tuple?

newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple2 = tuple('abcde')

print(newTuple)
print(newTuple2)
print(newTuple[-2]) # d
print(newTuple[1:3]) # ('b', 'c')
print(newTuple[:]) # ('a', 'b', 'c', 'd', 'e')

# How to traverse through a tuple?

for i in newTuple:
    print(i)

for i in range(len(newTuple)):
    print(newTuple[i])

# How to search for an element in a tuple?

print('a' in newTuple) # True
print('f' in newTuple) # False

print(newTuple.index('c')) # 2

def searchTuple(tuple, element):
    for i in range(0, len(tuple)):
        if tuple[i] == element:
            return print(f'The {element} is at index {i}')

    return 'The element was not found'

print(searchTuple(newTuple, 'c')) # The c is at index 2
print(searchTuple(newTuple, 'f')) # The element was not found