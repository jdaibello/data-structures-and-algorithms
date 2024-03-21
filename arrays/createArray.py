import array

arr1 = array.array('i', [1, 2, 3, 4, 5, 6])
arr2 = array.array('d', [1.3, 1.5, 1.6])

#arr1.insert(2, 9)
#print(arr1)

def traverseArray(array):
    for i in array:
        print(i)

def accessElement(array, index):
    if index >= len(array):
        print("Index out of range")
    else:
        print(array[index])

traverseArray(arr1)
accessElement(arr1, 2)

arr1.remove(4)
print(arr1)