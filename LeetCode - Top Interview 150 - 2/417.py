"""
[
[1,2,2,3,5],
[3,2,3,4,4],
[2,4,5,3,1],
[6,7,1,4,5],
[5,1,1,2,4]
]

memo = [
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
[0,0,0,0,0]
]

Increasing from pacific = 1
Increasing from atlantic = 2 (If it was 1, add to result)

=====

Time Complexity: O(mn + mn) = O(mn), Space Complexity: O(mn)
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = [[0, len(heights[0]) - 1], [len(heights) - 1, 0]]

        points = [[0 for _ in range(len(heights[0]))] for __ in range(len(heights))]

        for i in range(len(heights) - 1):
            self.bfs_reachable_point(i, 0, points, 0, 1)

        for j in range(1, len(heights[0]) - 1):
            self.bfs_reachable_point(0, j, points, 0, 1)

        for i in range(1, len(heights)):
            self.bfs_reachable_point(i, 0, points, 1, 2)

        for j in range(1, len(heights[0]) - 1):
            self.bfs_reachable_point(0, j, points, 1, 2)

        return result

    def bfs_reachable_point(points):
        pass


"""
I am not going to complete the implementation for now.

However, I think it would be great to remember the idea of moving from the outside in. The strategy is to mark the points reachable from the Pacific by changing 0 to 1, and then for points
reachable from the Atlantic, change 1 to 2. Finally, you just need to return the list of coordinates that have the value 2.
"""

"""
When implementing BFS using a queue, remember to mark a node as visited at the moment it is pushed into the queue, rather than after it is popped. This subtle difference can significantly
reduce the number of redundant operations.
"""

"""
I wanted to pass the time limit somehow, but it seems impossible to solve the problem using the current approach.

In the idea mentioned above, the points array can serve as a substitute for a visited array. However, in my approach, the memo array cannot be used as a replacement for visited. The biggest
limitation seems to be the necessity of creating an m X n array for every single execution.
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.num_rows = len(heights)
        self.num_cols = len(heights[0])
        self.memo = [["u" for _ in range(self.num_cols)] for __ in range(self.num_rows)]

        result = []

        for i in range(self.num_rows // 2):
            for j in range(self.num_cols // 2):
                if self.bfs_can_approach_both(i, j):
                    result.append([i, j])
                if self.bfs_can_approach_both(self.num_rows - 1 - i, j):
                    result.append([self.num_rows - 1 - i, j])
                if self.bfs_can_approach_both(i, self.num_cols - 1 - j):
                    result.append([i, self.num_cols - 1 - j])
                if self.bfs_can_approach_both(
                    self.num_rows - 1 - i, self.num_cols - 1 - j
                ):
                    result.append([self.num_rows - 1 - i, self.num_cols - 1 - j])

        if self.num_rows % 2 == 1:
            for j in range(self.num_cols):
                if self.bfs_can_approach_both(self.num_rows // 2, j):
                    result.append([self.num_rows // 2, j])

        if self.num_cols % 2 == 1:
            for i in range(self.num_rows):
                if self.num_rows % 2 == 1 and i == self.num_rows // 2:
                    continue

                if self.bfs_can_approach_both(i, self.num_cols // 2):
                    result.append([i, self.num_cols // 2])

        result = sorted(result)

        return result

    def bfs_can_approach_both(self, row, col):
        dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        visited = [[False for _ in range(self.num_cols)] for __ in range(self.num_rows)]
        visited[row][col] = True

        queue = deque()
        queue.append((row, col))

        can_pacific = False
        can_atlantic = False

        while queue:
            x, y = queue.popleft()

            if x == 0 or y == 0:
                can_pacific = True
            if x == self.num_rows - 1 or y == self.num_cols - 1:
                can_atlantic = True

            if self.memo[x][y] == "b":
                can_pacific = True
                can_atlantic = True
                continue
            elif self.memo[x][y] == "p":
                can_pacific = True
                continue
            elif self.memo[x][y] == "a":
                can_atlantic = True
                continue
            elif self.memo[x][y] == "x":
                continue

            for dx, dy in dxy:
                new_x = x + dx
                new_y = y + dy

                if (
                    0 <= new_x < self.num_rows
                    and 0 <= new_y < self.num_cols
                    and self.heights[new_x][new_y] <= self.heights[x][y]
                    and not visited[new_x][new_y]
                ):
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True

        if can_pacific and can_atlantic:
            self.memo[row][col] = "b"
        elif can_pacific:
            self.memo[row][col] = "p"
        elif can_atlantic:
            self.memo[row][col] = "a"
        else:
            self.memo[row][col] = "x"

        return can_pacific and can_atlantic


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.num_rows = len(heights)
        self.num_cols = len(heights[0])
        self.memo = [["u" for _ in range(self.num_cols)] for __ in range(self.num_rows)]

        result = []

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.bfs_can_approach_both(i, j):
                    result.append([i, j])

        return result

    def bfs_can_approach_both(self, row, col):
        dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        visited = [[False for _ in range(self.num_cols)] for __ in range(self.num_rows)]
        visited[row][col] = True

        queue = deque()
        queue.append((row, col))

        can_pacific = False
        can_atlantic = False

        while queue:
            x, y = queue.popleft()

            if x == 0 or y == 0:
                can_pacific = True
            if x == self.num_rows - 1 or y == self.num_cols - 1:
                can_atlantic = True

            if self.memo[x][y] == "b":
                can_pacific = True
                can_atlantic = True
                continue
            elif self.memo[x][y] == "p":
                can_pacific = True
                continue
            elif self.memo[x][y] == "a":
                can_atlantic = True
                continue
            elif self.memo[x][y] == "x":
                continue

            for dx, dy in dxy:
                new_x = x + dx
                new_y = y + dy

                if (
                    0 <= new_x < self.num_rows
                    and 0 <= new_y < self.num_cols
                    and self.heights[new_x][new_y] <= self.heights[x][y]
                    and not visited[new_x][new_y]
                ):
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True

        if can_pacific and can_atlantic:
            self.memo[row][col] = "b"
        elif can_pacific:
            self.memo[row][col] = "p"
        elif can_atlantic:
            self.memo[row][col] = "a"
        else:
            self.memo[row][col] = "x"

        return can_pacific and can_atlantic
