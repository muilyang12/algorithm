class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0

        max_profit = -math.inf

        while right < len(prices):
            max_profit = max(max_profit, prices[right] - prices[left])

            if prices[right] < prices[left]:
                left = right

            right += 1

        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_profit


"""
This is a very famous and important problem that can be solved using both DP and the Sliding Window approach.

First, let's look at the DP approach. If you want to solve the "Trapping Rain Water" problem using DP, you follow a similar logic. In that case, DP[i] represents the maximum height encountered up to
index i. Using that same intuition, you can treat min_price as the lowest price seen so far. Then, you constantly update the max_profit by calculating the difference between the current price and that
minimum price.

Next is the Sliding Window approach. I used to find the rule for updating the left pointer difficult, but it's actually quite simple if you look at it this way. The right pointer always increases by
one, acting much like a "current" index. If the value at right becomes smaller than the value at left, you simply update left to the position of right. There are core principles to keep in mind with
Sliding Windows, such as considering only the elements entering or leaving the window (at `left` and `right`) and moving the pointers after processing. In this specific case, you only need to focus on
the latter.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
                right += 1

        return max_profit
