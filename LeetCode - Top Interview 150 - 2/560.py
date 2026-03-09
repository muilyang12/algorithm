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