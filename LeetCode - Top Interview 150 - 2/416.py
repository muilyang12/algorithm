class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        target_sum = total_sum // 2

        memo = [False for i in range(target_sum + 1)]
        memo[total_sum] = True

        for num in nums:
            for i in range(target_sum, -1, -1):
                if memo[i] and i - memo > 0:
                    memo[i - memo] = True

        return memo[0]


"""
[1,5,11,5]

total_sum = 22
target_sum = 11

[T,F,F,F,F,T,T,F,F,F,T,T]
"""

"""
This problem is truly difficult. It feels like I need to go beyond just checking the idea and actually re-implement it.

One crucial point to remember is that the loop for `nums` must be the outer loop, not the inner one. Since each number can be used at most once, the loop for `memo` should be
the inner loop while the loop for `nums` remains the outer loop.

There are a few key elements to remember in Dynamic Programming.
1. You must derive the current `memo` value by referencing previous `memo` values. A method where you determine future `memo` values using the current value is not permitted.
2. When setting memo[i], you often need to use functions such as min or max, so you must be cautious when determining the initial values of the memo array.
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        target_sum = total_sum // 2

        memo = [False for i in range(target_sum + 1)]
        memo[0] = True

        for num in nums:
            for i in range(target_sum, num - 1, -1):
                if not memo[i - num]:
                    continue
                
                memo[i] = True

        return memo[target_sum]


"""
[1,2,3,5,9]

total_sum = 20

[T,F,F,F,F,F,F,F,F,F,F]
"""
