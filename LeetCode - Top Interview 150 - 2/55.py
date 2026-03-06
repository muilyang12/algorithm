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
