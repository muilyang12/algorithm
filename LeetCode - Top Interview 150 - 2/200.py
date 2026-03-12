class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(i, j)
                    result += 1

        return result

    def dfs(self, row: int, col: int):
        if row < 0 or row >= len(self.grid):
            return
        if col < 0 or col >= len(self.grid[0]):
            return
        if self.grid[row][col] != "1":
            return

        self.grid[row][col] = "3"

        self.dfs(row - 1, col)
        self.dfs(row + 1, col)
        self.dfs(row, col - 1)
        self.dfs(row, col + 1)
