"""
jump_count, reachable_with_current_count, max_rechable

When arrives at reachable_with_current_count, rwcc = mr

Updates mr like 55.
"""

# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0
        reachable_with_jump_count = 0
        max_reachable = -math.inf

        for i in range(len(nums)):
            max_reachable = max(max_reachable, i + nums[i])

            if i == reachable_with_jump_count and i != len(nums) - 1:
                jump_count += 1
                reachable_with_jump_count = max_reachable

        return jump_count


"""
There are two key elements to keep in mind.

1. This Greedy approach is an excellent idea. You need to use three variables, `jump_count`, `reachable_with_current_count`, and `max_reachable`.You are essentially building a
hierarchical structure of reachable zones.
2. An issue occurs when `max_reachable` exactly hits the last element of `nums` array. Since the for-loop reaches that point, it attempts one more jump and causes `jump_count`
to increment unnecessarily.
"""


# Time Complexity: O(n^2), Space Complexity: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        reachable = [(False, math.inf) for _ in nums]
        reachable[0] = (True, 0)

        for i in range(len(reachable)):
            if not reachable[i][0]:
                break

            max_reachable_from_i = min(i + nums[i], len(nums) - 1)
            for j in range(max_reachable_from_i, i, -1):
                reachable[j] = (True, min(reachable[j][1], reachable[i][1] + 1))

        return reachable[-1][1]
