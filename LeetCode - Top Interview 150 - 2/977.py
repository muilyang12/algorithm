"""
The easiest way to solve this problem is to do [num ** 2 for num in nums] and then use sorted. In that case it would have a time complexity of O(n log n). However after
thinking about it a bit more the following solution came to mind.

Since squares increase as they move away from 0 if I find the first positive value I can split the array into two parts which are from that point to the right and from
the element to its left to the far left. This turns the problem into something like "21. Merge Two Sorted Lists". In this case the time complexity becomes O(n). I think
I solved it really well.
"""


# Time Complexity: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first_positive = len(nums)

        if nums[0] > 0:
            first_positive = 0
        else:
            for i in range(len(nums)):
                if nums[i] > 0:
                    first_positive = i
                    break

        result = []

        i = first_positive
        j = first_positive - 1

        while i < len(nums) and j >= 0:
            right = nums[i] ** 2
            left = nums[j] ** 2

            if right < left:
                result.append(right)
                i += 1
            else:
                result.append(left)
                j -= 1

        while i < len(nums):
            right = nums[i] ** 2
            result.append(right)
            i += 1

        while j >= 0:
            left = nums[j] ** 2
            result.append(left)
            j -= 1

        return result
