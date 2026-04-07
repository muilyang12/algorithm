"""
max_reachable
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False for _ in nums]
        reachable[0] = True

        for i in range(len(reachable)):
            if not reachable[i]:
                break

            max_reachable = min(i + nums[i], len(reachable) - 1)
            
            for j in range(max_reachable, i, -1):
                if reachable[j]:
                    break
                
                reachable[j] = True

        return reachable[-1]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            
            max_reachable = max(max_reachable, i + nums[i])
        
        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0

        for index, num in enumerate(nums):
            if index > max_reachable:
                return False

            max_reachable = max(max_reachable, index + num)

        return True


"""
The more I solve LeetCode questions, the more I get a feel for how to solve certain types like Binary Search, DFS, and Graph. But DP is still quite tough, and Greedy is just insanely hard.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False for _ in range(len(nums))]
        memo[0] = True

        for i in range(len(memo)):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and memo[i]:
                    memo[i + j] = True

                if i + j == len(nums) - 1 and memo[i]:
                    return True

        return memo[-1]
