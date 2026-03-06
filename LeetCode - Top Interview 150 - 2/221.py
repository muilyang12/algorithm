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

"""
Initially, I implemented a method using three nested for-loops (size, i, j). However, after discussing it with Gemini, I found out if the top-left neighbor of a cell is already part of a square, I can probably build on that. My brute force implementation was O(M * N * min(M, N)), but I think that DP approach is O(M * N)."
"""