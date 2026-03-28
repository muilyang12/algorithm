"""
After solving the problem this way, I had a discussion with Gemini. The suggestion was to try solving it without maintaining the prefix sums in a separate array. In fact, the current
approach feels like it's unnecessarily looping through the array twice.
"""


# Time Complexity: O(2n) = O(n), Space Complexity: O(2n) = O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0 for _ in nums]
        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        result = 0

        hash = {0: [-1]}
        for index, prefix in enumerate(prefix_sum):
            if prefix - k in hash:
                result += len(hash[prefix - k])

            if prefix not in hash:
                hash[prefix] = []

            hash[prefix].append(index)

        return result


"""
Problems asking for the sum of a subarray can generally be solved in two ways.

First, there is the Sliding Window approach. To use a Sliding Window, the changes that occur when expanding the right side or shrinking the left side must be predictable. Because of this,
it typically requires conditions such as having only positive numbers or a sorted array.

Second, there is the Prefix Sum approach. While this increases the space complexity to $O(n)$, it has the advantage of not requiring any specific conditions on the values within the array,
unlike the Sliding Window method.
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {}
        hash[0] = [-1]

        result = 0

        current_sum = 0
        for index, num in enumerate(nums):
            current_sum += num
            if current_sum not in hash:
                hash[current_sum] = []

            if current_sum - k in hash:
                result += len(hash[current_sum - k])

            hash[current_sum].append(index)

        return result


"""
Should be contiguous?
All elements selected should be originally next to each other?
All numbers should be positive?
Negative can come?
Sorted?
"""

"""
Whenever I encounter problems involving subsequences, substrings, ors ubarrays, I must always ask about continuity. Keep this in mind!
"""

"""
Maybe it's because I've only solved this problem once. I missed the most crucial point. This problem cannot be solved using a Sliding Window. To use a Sliding Window for sums, you either need a sorted array or strictly positive values. That way, removing a value from the left and adding one to the right produces a consistent, predictable result. But since this problem has neither sorting nor exclusively positive numbers, Sliding Window is not an option.
"""

"""
The logic here is genius. Since the sum of a `subarray [i, j]` can be calculated as `prefixSum[j] - prefixSum[i-1]`, we can leverage this to solve the problem efficiently. What a great approach!
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)

        result = 0

        for i in range(len(nums)):
            temp_sum = 0
            for j in range(i, len(nums)):
                temp_sum += nums[j]

                if temp_sum == k:
                    result += 1

        return result