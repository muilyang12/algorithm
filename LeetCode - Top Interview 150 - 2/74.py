class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])

        left = 0
        right = numRows * numCols - 1

        while left <= right:
            mid = (left + right) // 2

            mid_row = mid // numCols
            mid_col = mid % numCols
            
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
