"""
I solved this problem alongside "46. Permutations" to compare them. If we were to treat each 1 as a distinct element based on its position, we could solve it exactly
like problem 46 by using indices. However, since we should not distinguish between identical values, using indices is not the right approach.

I proceeded with a solution that is as symmetrical to problem 46 as possible. The key differences are as follows.
1. A `counts` map was used instead of a `visited` set.
2. The logic skips the `current` iteration when `if counts[num] == 0`.
3. Most importantly, the loop iterates over `counts.keys()` instead of `for num in nums`.
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0

            counts[num] += 1

        self.result = []

        def dfs_backtracking(current, counts):
            if len(current) == len(nums):
                self.result.append(current[:])
                return

            for num in counts.keys():
                if counts[num] == 0:
                    continue

                current.append(num)
                counts[num] -= 1

                dfs_backtracking(current, counts)

                current.pop()
                counts[num] += 1

        dfs_backtracking([], counts)

        return self.result
