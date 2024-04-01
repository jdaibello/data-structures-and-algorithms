def heapify(customList, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and customList[left] < customList[smallest]:
        smallest = left

    if right < n and customList[right] < customList[smallest]:
        smallest = right

    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)

def heapSort(customList):
    n = len(customList)

    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i)

    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)

    customList.reverse()

customList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
heapSort(customList)
print(customList)