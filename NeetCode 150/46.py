class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs_backtrack(current, visited):
            nonlocal result

            if len(current) == len(nums):
                result.append(current[:])

            for i in range(len(nums)):
                if i in visited:
                    continue

                current.append(nums[i])
                visited.add(i)
                dfs_backtrack(current, visited)
                current.pop()
                visited.remove(i)

        dfs_backtrack([], set())

        return result
