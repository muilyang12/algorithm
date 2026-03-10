class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0

        result = math.inf

        current_sum = nums[right]

        while right < len(nums):
            while current_sum < target:
                right += 1
                if right >= len(nums):
                    break
                current_sum += nums[right]

            while current_sum >= target:
                result = min(result, right - left + 1)

                current_sum -= nums[left]
                left += 1

        return result if result != math.inf else 0

"""
Contiguous?
Integer?
Positive?
Should be equal to target?
"""

"""
7
[2,3,1,2,4,3], 9, 3
       !
           @
"""

"""
Just like we learned from the previous problem, whenever we see a word starting with 'sub-', the very first question we must ask is about contiguity!

To review what we learned, when there's a contiguity condition, the default approach is Prefix Sum. If we have additional conditions like Positive values or a Sorted array, then Sliding Window becomes a viable option.

This problem is slightly different. If we were looking for a sum exactly equal to the target, we could use a Hash Map to check if `current_sum - target` has occurred in the past based on `P[i] - P[j - 1] = target`. However, since this problem asks for a sum greater than the target, it should be solved using Sliding Window.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Prefix Sum Approach (i ~ j  = P[i] - P[j - 1])
        result = math.inf

        hash = {}
        hash[0] = [-1]

        current_sum = 0
        for index, num in enumerate(nums):
            current_sum += num

            print(num, current_sum, hash)
            if current_sum - target in hash:
                result = min(result, index - max(hash[current_sum - target]))

            if current_sum not in hash:
                hash[current_sum] = []

            hash[current_sum].append(index)

        return result if result != math.inf else 0