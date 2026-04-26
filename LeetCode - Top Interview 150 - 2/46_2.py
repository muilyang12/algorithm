"""
I solved this problem again to compare it with "47. Permutations II".

For problem 46 you define a function like `def dfs_backtracking(current, visited)` and proceed. In this case if a number is in `visited` you no longer add it to `current`.

On the other hand for problem 47 you define a function like def dfs_backtracking(current, counts) to proceed. Then if counts[num] == 0 you no longer add that number to
`current`. Up to this point the solution is symmetrical to that of 46. However there is one more point. You must use `for num in counts.keys()` instead of 
`for num in nums`. This is because you should not distinguish between the case where the first 1 is added followed by a dfs_backtracking call and the case where the
second 1 is added followed by the same call.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def dfs_backtracking(current, visited):
            if len(current) == len(nums):
                self.result.append(current[:])
                return

            for num in nums:
                if num in visited:
                    continue

                current.append(num)
                visited.add(num)

                dfs_backtracking(current, visited)

                current.pop()
                visited.remove(num)

        dfs_backtracking([], set())

        return self.result
