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