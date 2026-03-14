class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs_search(row, col, index, visited):
            if index >= len(word):
                return True
            if row < 0 or row >= len(board):
                return False
            if col < 0 or col >= len(board[0]):
                return False
            if board[row][col] != word[index]:
                return False
            if (row, col) in visited:
                return False

            visited.add((row, col))

            dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in dxy:
                if dfs_search(row + dx, col + dy, index + 1, visited):
                    return True

            visited.remove((row, col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs_search(i, j, 0, set()):
                    return True

        return False


"""
["A","B","C","E"]
["S","F","C","S"]
["A","D","E","E"]

["A","B","C","E"]
["S","F","E","S"]
["A","D","E","E"]
"""

"""
When using DFS with a `visited` set or array to explore all possible cumulative cases, it is essential to remove the current element from the `visited` at the end of the DFS. 
How many times do I have to keep making this same mistake?

In problem 78. Subsets, I used a `current` array to track cumulative cases. In that approach, I passed a copy of the array into each nested DFS call. If I had included the logic
to remove the element at the end of the DFS function, just like I did in this problem, there would have been no need to copy the array every time.

I've fixed that part and re-committed the code.
"""
