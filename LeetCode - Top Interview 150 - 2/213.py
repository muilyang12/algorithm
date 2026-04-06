"""
The suggestion was to maintain two separate memo arrays. One array assumes `nums[0]` is definitely included and the other assumes it is definitely excluded. I can then simply pick the maximum value between
those two results.

At first, I thought about using a structure like (value, True or False). However, Gemini pointed out that this could lead to the classic pitfall of greedy logic where the current local optimum isn't the 
global optimum. For instance, a lower value that is currently 'False' might actually result in a higher total later on compared to a higher value that is 'True'.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        memo1 = [0 for _ in nums]
        memo2 = [0 for _ in nums]

        memo1[0] = nums[0]
        memo1[1] = nums[0]
        memo1[2] = nums[0] + nums[2]

        memo2[0] = 0
        memo2[1] = nums[1]
        memo2[2] = nums[2]

        for i in range(3, len(nums)):
            memo1[i] = max(memo1[i - 2] + nums[i], memo1[i - 3] + nums[i])
            memo2[i] = max(memo2[i - 2] + nums[i], memo2[i - 3] + nums[i])

        return max(
            memo1[len(nums) - 1] - nums[len(nums) - 1],
            memo1[len(nums) - 2],
            memo2[len(nums) - 1],
            memo2[len(nums) - 2],
        )


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         memo = [0 for _ in nums]
#         memo[0] = (nums[0], True)
#         memo[1] = (nums[1], False)
#         memo[2] = (nums[0] + nums[2], True) if nums[0] + nums[2] > nums[1] else (nums[1], False)

#         for i in range(3, len(nums) - 1):
#             memo[i] = (memo[i - 2][0] + nums[i], memo[i - 2][1]) if memo[i - 2][0] > memo[i - 3][0] else (memo[i - 3][0] + nums[i], memo[i - 3][1])
