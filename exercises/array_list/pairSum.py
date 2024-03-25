"""
Find all pairs of an integer array whose sum is equal to a given number.
"""

def pairSum(myList, sum):
    result = []

    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(f'{myList[i]}+{myList[j]}')

    return result

arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pairSum(arr, target_sum)) # ['2+5', '4+3', '3+4', '-2+9']