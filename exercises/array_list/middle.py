"""
Return a new list that contains all but the first and last elements of the original list.
"""

def middle(lst):
    return lst[1:-1]

myList = [1, 2, 3, 4]
print(middle(myList)) # [2, 3]