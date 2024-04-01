def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        skipFisrtHouse = houseRobber(houses, currentIndex + 1)
        return max(stealFirstHouse, skipFisrtHouse)

houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 0)) # 41