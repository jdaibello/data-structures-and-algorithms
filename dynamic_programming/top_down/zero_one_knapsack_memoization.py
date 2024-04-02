class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zeroOneKnapsack(items, capacity, currentIndex, tempDict):
    dictKey = str(currentIndex) + str(capacity)

    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif dictKey in tempDict:
        return tempDict[currentIndex]
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zeroOneKnapsack(items, capacity - items[currentIndex].weight, currentIndex + 1, tempDict)
        profit2 = zeroOneKnapsack(items, capacity, currentIndex + 1, tempDict)
        tempDict[dictKey] = max(profit1, profit2)
        return tempDict[dictKey]
    else:
        return 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zeroOneKnapsack(items, 7, 0, {})) # 98