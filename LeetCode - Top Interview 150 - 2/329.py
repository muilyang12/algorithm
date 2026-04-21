"""
As with all DP problems, the most important step is how you define memo[i][j]. Initially, I defined memo[i][j] as the length of the Longest Increasing Path (LIP) ending at i, j, mainly because it seemed easier
to implement by carrying the path count through a visited set during DFS. However, that was not the most efficient approach.

A much better way is to store the length of the LIP starting from i, j in the memo. This way, you can use the true power of DP by immediately performing `return memo[i][j]` whenever you reach a coordinate that
has already been calculated.

To do this, you must update the memo while returning from the DFS rather than when entering it. In other words, the DFS function must be designed to return a specific value. I found it a bit difficult to make
the DFS return a value after not practicing for a while, but I need to get better at this.
"""

# Time Complexity: O(2mn) = O(mn), Space Complexity: O(mn)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[1 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]

        def dfs_get_lip_length(row, col):
            if memo[row][col] > 1:
                return memo[row][col]

            max_length = 0

            dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in dxy:
                new_row = row + dx
                new_col = col + dy

                if new_row < 0 or new_row >= len(matrix):
                    continue
                if new_col < 0 or new_col >= len(matrix[0]):
                    continue
                if matrix[new_row][new_col] <= matrix[row][col]:
                    continue

                new_length = dfs_get_lip_length(new_row, new_col)
                max_length = max(max_length, new_length)

            max_length += 1

            memo[row][col] = max_length

            return max_length

        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, dfs_get_lip_length(i, j))

        return result


"""
[3,4,5]
[3,2,6]
[2,2,1]

=====

[7,7,5]
[2,4,6]
[8,2,0]

[2,4,1]
[1,3,4]
[3,2,1]

???

[2, 5, 1]
[1, 4, 4]
[3, 3, 1]
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.result = -1

        memo = [[1 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]

        def dfs_get_lip(row, col, visited):
            if len(visited) + 1 < memo[row][col]:
                return

            visited.add((row, col))

            memo[row][col] = len(visited)
            self.result = max(self.result, memo[row][col])

            dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in dxy:
                new_row = row + dx
                new_col = col + dy

                if new_row < 0 or new_row >= len(matrix):
                    continue
                if new_col < 0 or new_col >= len(matrix[0]):
                    continue
                if matrix[new_row][new_col] <= matrix[row][col]:
                    continue

                dfs_get_lip(new_row, new_col, visited)

            visited.remove((row, col))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs_get_lip(i, j, set())

        return self.result
