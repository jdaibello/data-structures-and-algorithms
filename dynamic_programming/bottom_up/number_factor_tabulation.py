def numberFactor(n):
    tempArray = [1, 1, 1, 2]

    for i in range(4, n + 1):
        tempArray.append(tempArray[i - 1] + tempArray[i - 3] + tempArray[i - 4])

    return tempArray[n]

print(numberFactor(5)) # 6