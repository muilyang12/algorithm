class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        copied_matrix = [
            [int(matrix[i][j]) for j in range(len(matrix[0]))]
            for i in range(len(matrix))
        ]

        result = 0

        for i in range(len(copied_matrix)):
            for j in range(len(copied_matrix[0])):
                if copied_matrix[i][j] == 0:
                    continue

                if (
                    i > 0
                    and j > 0
                    and copied_matrix[i - 1][j] > 0
                    and copied_matrix[i - 1][j - 1] > 0
                    and copied_matrix[i][j - 1] > 0
                ):
                    copied_matrix[i][j] = (
                        min(
                            copied_matrix[i - 1][j],
                            copied_matrix[i - 1][j - 1],
                            copied_matrix[i][j - 1],
                        )
                        + 1
                    )

                result = max(result, copied_matrix[i][j])

        return result**2


"""
["1","0","1","0","0"]
["1","0","1","1","1"]
["1","1","1","1","1"]
["1","0","0","1","0"]

result = 2

["1","0","1","0","0"]
["1","0","1","1","1"]
["1","1","1","2","2"]
["1","0","0","1","0"]

Edge cases
[["1"]]
[["0"]]
[
    ["1","0"],
    ["0","0"]
]
[["0","1"]]
"""

"""
The key idea here is to build the DP memo based on the bottom-right corner of the square.
"""

"""
Initially, I implemented a method using three nested for-loops (size, i, j). However, after discussing it with Gemini, I found out if the top-left neighbor of a cell is already part of a square, I can probably build on that. My brute force implementation was O(M * N * min(M, N)), but I think that DP approach is O(M * N)."
"""

"""
I didn't use this for this specific problem, but I'm leaving a note here as a reminder. In Python, you can represent infinity using `math.inf`. Keep this in mind!
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.matrix = matrix
        self.numRows = len(matrix)
        self.numCols = len(matrix[0])

        result = 0

        for size in range(1, min(self.numRows, self.numCols) + 1):
            current_result = self.handleSize(size)
            if current_result:
                result = size**2
            else:
                break

        return result

    def handleSize(self, size):
        for i in range(self.numRows - size + 1):
            for j in range(self.numCols - size + 1):
                if self.areAllOne(i, j, size):
                    return True

        return False

    def areAllOne(self, row: int, col: int, size: int) -> bool:
        if row + size - 1 >= self.numRows or col + size - 1 >= self.numCols:
            return False

        for i in range(row, row + size):
            for j in range(col, col + size):
                if self.matrix[i][j] != "1":
                    return False

        return True


"""
["1","0","1","0","0"]
["1","0","1","1","1"]
["1","1","1","1","1"]
["1","0","0","1","0"]

4, 5

for i
for j

result = 1

Edge
0x0
1x1 - "1", "0"
"""
