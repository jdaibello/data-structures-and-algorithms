"""
Remove the duplicate numbers on given integer array/list
"""

def removeDuplicates(arr):
    uniqueList = []
    seen = set()

    for i in arr:
        if i not in seen:
            uniqueList.append(i)
            seen.add(i)

    return uniqueList

myList = [1, 1, 2, 2, 3, 4, 5]
print(removeDuplicates(myList)) # [1, 2, 3, 4, 5]