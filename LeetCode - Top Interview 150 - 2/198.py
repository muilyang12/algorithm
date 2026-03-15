class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        memo = [num for num in nums]
        memo[2] = nums[0] + nums[2]

        result = max(memo[0], memo[1], memo[2])
        for i in range(3, len(nums)):
            memo[i] = max(memo[i - 3] + nums[i], memo[i - 2] + nums[i])
            result = max(result, memo[i])

        return result


"""
nums = [2,7,9,3,1]
                ^

"Accumulation" from the beginning => DP

memo = [2,7,0,0,0]

=====

nums = [2,100,9,3,100]
memo[i] = max profit when he robs that house

memo = [2, 100, 11, 103, 200]
"""

"""
This is a very famous DP problem. As I've mentioned before, the core of any DP problem is clearly defining DP[i]. In this solution, 
I defined DP[i] as the maximum profit when the $i$-th house is robbed.
"""

"""
In this problem, DP[i] is defined as the profit gained when the i-th house is robbed. Since you can't rob two houses in a row, you
have to compare the options. "Robbing the house two steps back and the current one" vs "Robbing the house three steps back and the
current one". By finding the maximum between these two paths, I can determine the optimal profit for that position.
"""
