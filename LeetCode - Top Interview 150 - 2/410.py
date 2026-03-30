class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum, subarray_count):
            count_left = subarray_count
            current_sum = 0
            for num in nums:
                current_sum += num

                if current_sum > max_sum:
                    count_left -= 1
                    current_sum = num

            if count_left <= 0:
                return False
            else:
                return True

        left = max(nums)
        right = sum(nums)

        result = math.inf

        while left <= right:
            mid = (left + right) // 2

            if can_split(mid, k):
                result = min(result, mid)

                right = mid - 1
            else:
                left = mid + 1

        return result


"""
Have to understand "Subarray vs Subsequence vs Subset"

Subarray: A contiguous part of the original array.
Subsequence: Elements derived from an array while maintaining the relative order, but not necessarily contiguous.
Subset: Any collection of elements from the original array, regardless of order or continuity.
"""

"""
I mistakenly thought about this problem as if I had to split the array into exactly two subarrays. If that were the case, it would be correct to split it based on indices. However, since k might not
be 2, I need to take a different approach.
"""

"""
The strategy is to start with `left = max(nums)` and `right = sum(nums)` and then test the values in between. During this process, binary search is used to find the most appropriate value. This involves
creating a function like `can_split(max_sum, k)` to check whether the array can be partitioned into k or fewer subarrays such that the sum of each part does not exceed max_sum.

Writing the can_split function also seems difficult. However, I learned that I can use a Greedy approach by counting from the front and making a cut whenever the sum exceeds `max_sum`.

Looking at it this way, this problem feels truly challenging because it requires using both Binary Search and Greedy concepts together.

The solution to this problem is almost identical to the approach used in "1011. Capacity To Ship Packages Within D Days".
"""
