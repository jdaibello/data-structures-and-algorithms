shoppingList = ['Milk', 'Cheese', 'Butter']

print(shoppingList)
print(shoppingList[1])
print('Milk' in shoppingList)
print(shoppingList[-1]) # Last element

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + '+'
    print(shoppingList[i])

# Update/Insert

myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)

myList[2] = 33 # Update
myList[4] = 55 # Update
print(myList)

myList.insert(0, 11) # Insert 11 at index 0
myList.append(55) # Add to the end

newList = [11, 12, 13, 14]
myList.extend(newList) # Add all elements of newList to myList
print(myList)

# Slice/Delete

myList2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList2[0:2]) # 0 to 1
print(myList2[1:]) # 1 to end
print(myList2[:3]) # 0 to 2
print(myList2[:]) # All

myList2.pop(1) # Remove element at index 1
print(myList2.pop()) # Remove and return last element
print(myList2)

del myList2[2:4] # Remove elements from index 2 to 3
print(myList2)

myList2.remove('c') # Remove element 'c'
print(myList2)

# Searching for an element in a list

myList3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# in operator
target = 50

if target in myList3:
    print(f'{target} is in the list')
else:
    print(f'{target} is not in the list')

# Linear search
def linearSearch(list, target):
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1

print(linearSearch(myList3, target))

# List operations / functions

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b # Concatenation
print(c)

d = [0, 1]
d = d * 4 # Repetition
print(d)

e = [0, 1, 2, 3, 4, 5, 6]
print(len(e)) # Length
print(max(e)) # Highest value
print(min(e)) # Lowest value
print(sum(e)) # Sum of all elements
print(sum(e) / len(e)) # Average

myList4 = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    myList4.append(value)

average = sum(myList4) / len(myList4)
print(f'Average: {average}')

# String and Lists

f = 'spam'
g = list(f)
print(g)

h = 'spam-spam1-spam2'
delimiter = 'a'
i = h.split(delimiter) # Split by delimiter
print(i)
print(delimiter.join(i)) # Join by delimiter