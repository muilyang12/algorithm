class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # for i
        #     for j
        #         if board[i][j] == "O"
        #             dfs("O", "A")
        
        # for i
        #     if board[i][0] == "A"
        #         dfs("A", "O")
        #     if board[i][len - 1] == "A"
        #         dfs("A", "O")

        # for j
        #     if board[0][j] == "A"
        #         dfs("A", "O")
        #     if board[len - 1][j] == "A"
        #         dfs("A", "O")

        # for i
        #     for j
        #         if board[i][j] == "A"
        #             board[i][j] = "X"


"""
For this problem, I need to keep the core idea in mind. First, process the grid using a standard DFS or BFS. Then, perform an additional DFS starting from the edges to restore the areas
that are connected to the boundary.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(row, col, from_char, to_char):
            board[row][col] = to_char

            dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in dxy:
                new_row = row + dx
                new_col = col + dy

                if new_row < 0 or new_row >= len(board):
                    continue
                if new_col < 0 or new_col >= len(board[0]):
                    continue
                if board[new_row][new_col] == from_char:
                    dfs(new_row, new_col, from_char, to_char)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    dfs(i, j, "O", "Z")

        for i in range(len(board)):
            if board[i][0] == "Z":
                dfs(i, 0, "Z", "O")
            if board[i][len(board[0]) - 1] == "Z":
                dfs(i, len(board[0]) - 1, "Z", "O")

        for j in range(1, len(board[0]) - 1):
            if board[0][j] == "Z":
                dfs(0, j, "Z", "O")
            if board[len(board) - 1][j] == "Z":
                dfs(len(board) - 1, j, "Z", "O")

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "Z":
                    board[i][j] = "X"


"""
['X', 'X', 'X', 'X']
['X', 'O', 'O', 'X']
['X', 'X', 'O', 'X']
['X', 'O', 'X', 'X']

['X', 'X', 'X', 'X']
['X', 'Z', 'Z', 'X']
['X', 'X', 'Z', 'X']
['X', 'Z', 'X', 'X']

['X', 'X', 'X', 'X']
['X', 'Z', 'Z', 'X']
['X', 'X', 'Z', 'X']
['X', 'O', 'X', 'X']
"""
