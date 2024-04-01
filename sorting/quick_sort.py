def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]

def pivot(list, pivotIndex, endIndex):
    swapIndex = pivotIndex

    for i in range(pivotIndex + 1, endIndex + 1):
        if list[i] < list[pivotIndex]:
            swapIndex += 1
            swap(list, swapIndex, i)

    swap(list, pivotIndex, swapIndex)
    return swapIndex

def quickSort(list, left, right):
    if left < right:
        pivotIndex = pivot(list, left, right)
        quickSort(list, left, pivotIndex - 1)
        quickSort(list, pivotIndex + 1, right)
    return list

customList = [3, 5, 0, 6, 2, 1, 4]
print(quickSort(customList, 0, len(customList) - 1))