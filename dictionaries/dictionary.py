import random

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

# Dictionary methods

myDict = {'name': 'Jack', 'age': 26, 'address': 'London', 'education': 'Engineering'}

# myDict.clear() # Removes all elements from dictionary
print(myDict)

myDict2 = myDict.copy() # Returns a shallow copy of dictionary
print(myDict2)

newDict = {}.fromkeys([1, 2, 3], 0) # Create a new dictionary with keys from sequence and values set to value
print(newDict)

print(myDict2.get('age', 27)) # Returns the value of the specified key. If key does not exist, returns default value

print(myDict2.items()) # Returns a new view of the dictionary items as a Tuple (key, value)

print(myDict2.keys()) # Returns keys of dictionary

print(myDict2.popitem()) # Removes the last key-value pair from dictionary and returns it as Tuple
print(myDict2)

myDict2.setdefault('address', 'London') # Returns the value of the specified key. If key does not exist, inserts key with specified value
print(myDict2)

print(myDict2.values()) # Returns a list of dictionary values

newDict2 = {'a': 1, 'b': 2, 'c': 3}
myDict2.update(newDict2)
print(myDict2) # Updates the dictionary with other dictionary

# Dictionary operations

myDict3 = {
    3: 'three',
    5: 'five',
    9: 'nine',
    2: 'two',
    1: 'one',
    4: 'four'
}

print('ten' not in myDict3.values()) # Check if value not exists in dictionary
print(len(myDict3)) # Length of dictionary
print(all(myDict3)) # Returns True if all keys of dictionary are True
print(any(myDict3)) # Returns True if any key of dictionary is True
print(sorted(myDict3)) # Returns a new sorted list of keys in dictionary


# Dictionary comprehension

cityNames = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

cityTemps = {city: random.randint(20, 30) for city in cityNames}
print(cityTemps)

above25 = {city: temp for (city, temp) in cityTemps.items() if temp > 25}
print(above25)