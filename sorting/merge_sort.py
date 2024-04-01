def merge(customList, left, middle, right):
    number1 = middle -left + 1
    number2 = right - middle

    leftList = [0] * (number1)
    rightList = [0] * (number2)

    for i in range(0, number1):
        leftList[i] = customList[left + i]

    for j in range(0, number2):
        rightList[j] = customList[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while i < number1 and j < number2:
        if leftList[i] <= rightList[j]:
            customList[k] = leftList[i]
            i += 1
        else:
            customList[k] = rightList[j]
            j += 1
        k += 1

    while i < number1:
        customList[k] = leftList[i]
        i += 1
        k += 1

    while j < number2:
        customList[k] = rightList[j]
        j += 1
        k += 1

def mergeSort(customList, left, right):
    if left < right:
        middle = (left + (right - 1)) // 2
        mergeSort(customList, left, middle)
        mergeSort(customList, middle + 1, right)
        merge(customList, left, middle, right)
    return customList

customList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(mergeSort(customList, 0, 8))