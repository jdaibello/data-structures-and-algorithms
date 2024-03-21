import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1) # Insert a new column at the beginning
threeDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0) # Insert a new row at the beginning
print(newTwoDArray)
print(threeDArray)

def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])

def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "Value found at index " + str(i) + ", " + str(j)
    return "Value not found"

accessElement(twoDArray, 2, 3)
traverseArray(twoDArray)
print(searchTDArray(twoDArray, 14))

newTDArray = np.delete(twoDArray, 1, axis=1) # Delete the second column
print(newTDArray)