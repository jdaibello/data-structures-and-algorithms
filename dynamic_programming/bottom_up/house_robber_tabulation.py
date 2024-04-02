def houseRobber(houses, currentIndex):
    tempArray = [0] * (len(houses) + 2)

    for i in range(len(houses) - 1, -1, -1):
        tempArray[i] = max(houses[i] + tempArray[i + 2], tempArray[i + 1])

    return tempArray[0]

houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 0)) # 41