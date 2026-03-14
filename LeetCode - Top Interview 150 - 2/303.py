class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]

"""
Honestly, I saw the solution instantly because I came in so prepared for Prefix Sum.

Still, I must remember the ideal logical flow. The goal is to calculate the sum from left to right. If you think about it, you have to use the sum up to left while calculating the sum up to right.
This is essentially DP. Since it involves cumulative sums or products, it's a classic Prefix Sum style problem.
"""