"""
Given a square matrix, calculate the sum of the diagonal elements.
"""

def diagonalSum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

my2DList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonalSum(my2DList)) # 15