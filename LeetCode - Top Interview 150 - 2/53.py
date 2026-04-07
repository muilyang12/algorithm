"""
start_point, current_sum, result

for:
cs < 0
sp = i
cs = nums[i]

r = max(r, cs)
"""


# Time Complexity: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -math.inf
        current_sum = -math.inf

        for num in nums:
            if current_sum < 0:
                current_sum = num
            else:
                current_sum += num

            result = max(result, current_sum)

        return result


"""
Kadane's Algorithm

If you know this problem should be solved with a Greedy approach, the idea is intuitive enough. However, without that knowledge, it feels incredibly difficult to solve. The real
challenge with Greedy is determining whether the current best option will hinder the future optimal solution or remain the best choice overall.

Through my discussion with Gemini, I was advised to consider whether a reversal of choice is ever necessary. In this problem, if the current_sum becomes negative at any point,
the subarray accumulated up to that point acts as a sort of debt. It no longer helps in finding the largest sum. Since there is essentially no possibility of needing to reverse
this decision, a Greedy approach is valid for this problem.
"""

"""
At first glance, I considered using the Prefix Sum approach, similar to how I solved "560. Subarray Sum Equals K".
"""


# Time Complexity: O(n^2)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prefix = [0]

        current_sum = 0
        for num in nums:
            current_sum += num
            prefix.append(current_sum)

        result = -math.inf

        for i in range(1, len(prefix)):
            for j in range(i - 1):
                result = max(result, prefix[i] - prefix[j])

        return result
