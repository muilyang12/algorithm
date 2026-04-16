class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.result = 0

        def bfs_calculate_perimeter(row, col):
            dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            queue = deque()
            queue.append((row, col))
            grid[row][col] = 3

            while queue:
                x, y = queue.popleft()

                for dx, dy in dxy:
                    new_x = x + dx
                    new_y = y + dy

                    if new_x < 0 or new_y < 0:
                        self.result += 1
                    elif new_x >= len(grid) or new_y >= len(grid[0]):
                        self.result += 1
                    elif grid[new_x][new_y] == 0:
                        self.result += 1
                    elif grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 3

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    bfs_calculate_perimeter(i, j)

        return self.result
