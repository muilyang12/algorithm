"""
This problem is a Sliding Window + Hash problem. I must remember this.

1. You should only consider what comes in and goes out from the left and right. Recomputing everything every cycle is not allowed.
2. The pointers must be moved only after the processing is done.
3. Use a for-loop for the outer structure. If it's a variable-size window, use an additional while-loop inside.
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited_nums = set()

        left = 0

        for right in range(len(nums)):
            if right - left > k:
                visited_nums.remove(nums[left])
                left += 1

            if nums[right] in visited_nums:
                return True

            visited_nums.add(nums[right])

        return False


"""
nums = [1,2,3,1,2,3]
        !
        @
"""

"""
Can k be larger than len(nums)?
k is positive?
"""

"""
nums = [1,2,3,1], k = 3
"""
