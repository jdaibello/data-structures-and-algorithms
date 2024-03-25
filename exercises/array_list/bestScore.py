"""
Get the first and second best scores from a list of scores.
"""

def firstSecondBest(scores):
    scores.sort(reverse=True)
    return scores[:2]

myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(firstSecondBest(myList)) # [90, 87]