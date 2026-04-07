"""
dfs(temp, visited)

for num in nums:
    if visited:
        continue

    temp.append(num)
    visited.add(num)

    dfs(temp)

    temp.pop()

"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs_permute(result, temp, visited):
            for num in nums:
                if num in visited:
                    continue

                temp.append(num)
                visited.add(num)

                if len(temp) == len(nums):
                    result.append(temp[:])

                dfs_permute(result, temp, visited)

                temp.pop()
                visited.remove(num)

        result = []
        dfs_permute(result, [], set())

        return result
