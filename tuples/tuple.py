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