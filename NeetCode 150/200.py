class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        def bfs_fill(row, col):
            nonlocal result
            result += 1

            queue = deque()
            queue.append((row, col))

            dij = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                i, j = queue.popleft()

                for di, dj in dij:
                    new_i = i + di
                    new_j = j + dj

                    if new_i < 0 or new_i >= len(grid):
                        continue
                    elif new_j < 0 or new_j >= len(grid[0]):
                        continue
                    elif grid[new_i][new_j] != "1":
                        continue

                    grid[new_i][new_j] = "2"
                    queue.append((new_i, new_j))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs_fill(i, j)

        return result
