class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_orange_count = 0

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

                if grid[i][j] == 1:
                    fresh_orange_count += 1

        elapsed_time = 0

        while queue:
            current_length = len(queue)

            for _ in range(current_length):
                row, col = queue.popleft()

                dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in dxy:
                    new_row = row + dx
                    new_col = col + dy

                    if new_row < 0 or new_row >= len(grid):
                        continue
                    if new_col < 0 or new_col >= len(grid[0]):
                        continue
                    if grid[new_row][new_col] != 1:
                        continue

                    grid[new_row][new_col] = 2
                    fresh_orange_count -= 1

                    queue.append((new_row, new_col))

            elapsed_time = elapsed_time + 1 if len(queue) > 0 else elapsed_time

        return elapsed_time if fresh_orange_count == 0 else -1


"""
[2,1,1]
[0,1,1]
[1,0,1]

[2,1,1]
[0,1,1]
[1,0,1]
"""

"""
I had a rough idea of how to solve this at first glance, but I failed to organize my strategy systematically. For these graph problems, both BFS and DFS should be considered. Since I personally prefer DFS,
I jumped straight into it without weighing both options.

I soon realized DFS might be problematic and tried to 'tweak' it. My idea was to use a while loop with nested for-loops, which would result in O(T X N^2) complexity, where T is the elapsed time. Honestly,
this approach isn't necessarily 'bad' in terms of logic. However, this problem requires all 'rotten' nodes to spread one step at a time simultaneously unlike 'Number of Islands'. This is a classic BFS
scenario. I need to be equally proficient in both DFS and BFS.
"""
