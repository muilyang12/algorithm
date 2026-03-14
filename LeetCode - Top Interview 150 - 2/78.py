class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(current, target_index, result):
            if target_index >= len(nums):
                result.append(current)
                return

            dfs([c for c in current], target_index + 1, result)
            new_current = [c for c in current]
            new_current.append(nums[target_index])
            dfs(new_current, target_index + 1, result)

        result = []
        dfs([], 0, result)

        return result

"""
This problem is really interesting. For this type of backtracking problem, using DFS is the standard approach. The interesting approach here is calling DFS once before adding a specific element 
and then calling it again after adding it. Since I'm calling DFS without adding an element, I cannot determine the target character using the current's length. This is why I need to pass 
target_index as a separate parameter. I think I solved this one quite well.
"""
