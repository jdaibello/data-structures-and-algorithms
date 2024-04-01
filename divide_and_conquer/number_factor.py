def numberFactor(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        subProblem1 = numberFactor(n - 1)
        subProblem2 = numberFactor(n - 3)
        subProblem3 = numberFactor(n - 4)
        return subProblem1 + subProblem2 + subProblem3

print(numberFactor(5)) # 6