def numberFactor(n, tempDict):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in tempDict:
            subProblem1 = numberFactor(n - 1, tempDict)
            subProblem2 = numberFactor(n - 3, tempDict)
            subProblem3 = numberFactor(n - 4, tempDict)
            tempDict[n] = subProblem1 + subProblem2 + subProblem3
        return tempDict[n]

print(numberFactor(5, {})) # 6