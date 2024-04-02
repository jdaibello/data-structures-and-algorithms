def houseRobber(houses, currentIndex, tempDict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            stealCurrentHouse = houses[currentIndex] + houseRobber(houses, currentIndex + 2, tempDict)
            skipCurrentHouse = houseRobber(houses, currentIndex + 1, tempDict)
            tempDict[currentIndex] = max(stealCurrentHouse, skipCurrentHouse)
        return tempDict[currentIndex]

houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 0, {})) # 41