class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs_get_area(row, col):
            area = 0

            queue = deque()
            queue.append((row, col))

            dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                row, col = queue.popleft()

                area += 1

                for dx, dy in dxy:
                    if (
                        0 <= row + dx < len(grid)
                        and 0 <= col + dy < len(grid[0])
                        and grid[row + dx][col + dy] == 1
                    ):

                        grid[row + dx][col + dy] = 3
                        queue.append((row + dx, col + dy))

            return area

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 3
                    area = bfs_get_area(i, j)
                    result = max(result, area)

        return result


"""
From a purely logical perspective, it might seem more elegant to handle the `grid[][] = 3` update inside the `while queue` loop, which is how I implemented it below. However,
that approach leads to an issue where the same coordinates are pushed into the queue multiple times. Although the `if grid[row][col] != 1` condition prevents errors, it results
in unnecessary overhead for both runtime and memory. This is why Gemini suggested updating the values at the moment they are pushed into the queue.

When solving 2D graph problems using BFS with a queue, you must remember to update the `visited` array at the same time you push the element into the queue. This is a crucial
point to keep in mind.
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_area(row, col):
            area = 0

            queue = deque()
            queue.append((row, col))

            dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                row, col = queue.popleft()

                if grid[row][col] != 1:
                    continue

                grid[row][col] = 3
                area += 1

                for dx, dy in dxy:
                    if 0 <= row + dx < len(grid) and 0 <= col + dy < len(grid[0]):
                        queue.append((row + dx, col + dy))

            return area

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = get_area(i, j)
                    result = max(result, area)

        return result
