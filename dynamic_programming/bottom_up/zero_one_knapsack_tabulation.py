class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zeroOneKnapsack(profits, weights, capacity):
    if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return 0

    numberOfRows = len(profits) + 1
    dp = [[None for i in range(capacity + 2)] for j in range(numberOfRows)]

    for i in range(numberOfRows):
        dp[i][0] = 0

    for i in range(capacity + 1):
        dp[numberOfRows - 1][i] = 0

    for row in range(numberOfRows - 2, -1, -1):
        for column in range(1, capacity + 1):
            profit1 = 0
            profit2 = 0

            if weights[row] <= column:
                profit1 = profits[row] + dp[row + 1][column - weights[row]]

            profit2 = dp[row + 1][column]
            dp[row][column] = max(profit1, profit2)
    return dp[0][capacity]

profits = [31, 26, 72, 17]
weights = [3, 1, 5, 2]

print(zeroOneKnapsack(profits, weights, 7)) # 98