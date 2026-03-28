class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]

        self.prefix[0][0] = matrix[0][0]
        for i in range(1, len(matrix)):
            self.prefix[i][0] = matrix[i][0] + self.prefix[i - 1][0]
        for j in range(1, len(matrix[0])):
            self.prefix[0][j] = matrix[0][j] + self.prefix[0][j - 1]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.prefix[i][j] = (
                    matrix[i][j]
                    + self.prefix[i - 1][j]
                    + self.prefix[i][j - 1]
                    - self.prefix[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = (
            self.prefix[row2][col2]
            - (self.prefix[row2][col1 - 1] if col1 - 1 >= 0 else 0)
            - (self.prefix[row1 - 1][col2] if row1 - 1 >= 0 else 0)
            + (self.prefix[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0)
        )

        return result


"""
I thought the approach below would work, but it turns out that it results in a time complexity of $O(h)$ for the sumRegion function, which violates the constraints of the problem. In other
words, I cannot approach this by calculating the prefix sums row by row.
"""


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]
        for i in range(len(matrix)):
            self.prefix[i][0] = matrix[i][0]

        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.prefix[i][j] = self.prefix[i][j - 1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for i in range(row1, row2 + 1):
            result += self.prefix[i][col2] - (self.prefix[i][col1 - 1] if col1 - 1 >= 0 else 0)

        return result


"""
This problem clearly points toward using Prefix Sum. The requirement that "sumRegion works in $O(1)$ time complexity" implies that the sums must be precalculated in advance. In other words,
it is telling us to solve it using the Prefix Sum method.
"""

"""
[3, 3, 4, 8, 10]
[5, 11, 14, 16, 17]
[1, 3, 3, 4, 9]
[4, 5, 5, 6, 13]
[1, 1, 4, 4, 9]]
"""
