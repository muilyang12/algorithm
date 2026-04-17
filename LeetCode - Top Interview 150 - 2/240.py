"""
This problem seems to require a specific approach that is worth memorizing.

You must remember to start from the top-right corner of the matrix. If the `target` is greater than the `current` value, you move down by performing `current_row += 1`. If
the `target` is smaller than the `current` value, you move to the left by performing `current_col -= 1`.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        current_row = 0
        current_col = len(matrix[0]) - 1

        while current_row < len(matrix) and current_col >= 0:
            current = matrix[current_row][current_col]

            if current == target:
                return True
            elif current > target:
                current_col -= 1
            else:
                current_row += 1

        return False
