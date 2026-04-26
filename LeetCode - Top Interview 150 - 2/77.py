"""
I decided to solve this problem alongside "46. Permutations" to compare the two.

In the Permutations problem I used a `visited` set to skip numbers that had already been used since the loop iterates through the entire nums array every time. However
in the Combinations problem I can use a `start_index` instead of a `visited` set. For example if 2 is chosen as the first value the previous value 1 should not be
included in the current combination. By passing `3` for the start_index in the next recursive call, we ensure that the same number is not reconsidered in the loop,
making the `visited` set completely unnecessary.

If you keep this one thing in mind this problem can be solved quite easily.
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []

        def dfs_backtracking(current, start):
            if len(current) == k:
                self.result.append(current[:])
                return

            for i in range(start, n + 1):
                current.append(i)

                dfs_backtracking(current, i + 1)

                current.pop()

        dfs_backtracking([], 1)

        return self.result
