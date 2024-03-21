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