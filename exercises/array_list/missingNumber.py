"""
Write a function to find the missing number in a given integer array of 1 to 100.
The function takes to parameter the array and the number of elements that needs to be in array.
For example if we want to find missing number from 1 to 6 the second parameter will be 6.
"""

def missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

print(missing_number([1, 2, 3, 4, 6], 6))