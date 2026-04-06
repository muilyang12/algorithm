"""
Basically, since it's a backtracking problem, using DFS is a bit of an obvious choice, so it's relatively easy to set up the logic. The key element to remember here is that the DFS function must be written based on
the rows.

def dfs(row):
    for col in range(n):

It's crucial to understand that the function should be structured this way. As long as I keep this in mind, the rest of the problem seems manageable.
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs_queens(row, result, board, visited_col, visited_p_diag, visited_n_diag):
            if row == n:
                result.append(["".join(row) for row in board])
                return

            for col in range(n):
                if col in visited_col:
                    continue
                if row + col in visited_p_diag or row - col in visited_n_diag:
                    continue

                board[row][col] = "Q"
                visited_col.add(col)
                visited_p_diag.add(row + col)
                visited_n_diag.add(row - col)

                dfs_queens(
                    row + 1, result, board, visited_col, visited_p_diag, visited_n_diag
                )

                board[row][col] = "."
                visited_col.remove(col)
                visited_p_diag.remove(row + col)
                visited_n_diag.remove(row - col)

        result = []
        board = [["." for _ in range(n)] for __ in range(n)]
        dfs_queens(0, result, board, set(), set(), set())

        return result
