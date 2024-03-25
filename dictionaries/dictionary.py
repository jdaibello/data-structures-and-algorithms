# Creating Dictionary

myDict = dict()
print(myDict)

myDict2 = {}
print(myDict2)

engSp = dict(one='uno', two='dos', three='tres')
print(engSp)

engSp2 = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(engSp2)

engSpList = [('one', 'uno'), ('two', 'dos'), ('three', 'tres')]
print(dict(engSpList))

# Update / add elements in dictionary

myDict = {'name': 'Jack', 'age': 26}
myDict['name'] = 'John'
myDict['address'] = 'London'
print(myDict)

# Traverse dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

# Search value in dictionary

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value

    return 'The value does not exist'

print(searchDict(myDict, 'John'))

# Delete elements from dictionary

del myDict['age']
print(myDict)

removedElement = myDict.pop('address')
print(removedElement)
print(myDict)