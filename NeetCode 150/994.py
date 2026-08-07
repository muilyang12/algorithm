class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        result = 0

        while queue:
            length = len(queue)
            for _ in range(length):
                i, j = queue.popleft()

                dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in dxdy:
                    x, y = i + dx, j + dy
                    if x < 0 or x >= len(grid):
                        continue
                    if y < 0 or y >= len(grid[0]):
                        continue
                    if grid[x][y] == 0 or grid[x][y] == 2:
                        continue

                    grid[x][y] = 2
                    queue.append((x, y))

            if length
            result += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return (result - 1) if result > 0 else result
