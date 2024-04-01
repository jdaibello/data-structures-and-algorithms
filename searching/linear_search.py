def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(linearSearch([20, 40, 30, 50, 90], 90)) # 4