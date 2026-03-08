class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1 for _ in range(len(nums))]
        result = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)
                    result = max(result, memo[i])

        return result


"""
Positive numbers?
"""

"""
DP

[]

Array

i th value relies on i-1 th value.

a_{n} = a_{n-1} + ...
"""

"""
[10,9,2,5,3,7,101,18]
  1 1 1 1 1 1   1  1
    1 1 2 2 3   4  4
"""

"""
In this case, memo[i] represents the maximum length of an Increasing Subsequence that ends with the $i$-th element. In array-based DP, memo[i] often denotes a state where the current element is the last element of the sequence. Let's keep this in mind.
"""
