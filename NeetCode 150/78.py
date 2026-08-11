class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs_backtrack(index, current):
            nonlocal result

            if index == len(nums):
                result.append(current[:])
                return

            dfs_backtrack(index + 1, current)

            current.append(nums[index])
            dfs_backtrack(index + 1, current)
            current.pop()

        dfs_backtrack(0, [])

        return result
