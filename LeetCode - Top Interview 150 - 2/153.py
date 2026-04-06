"""
In problems where you have to find something in a Rotated Sorted Array, the key is proper case analysis.

[0,1,2,3,4,5,6]
       ^
[4,5,6,0,1,2,3]
       ^
[2,3,4,5,6,0,1]
       ^
[5,6,0,1,2,3,4]
       ^
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif mid == 0 and nums[mid] < nums[-1]:
                return nums[mid]

            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1


"""
[0,1,2,3,4,5,6,7,8,9]
 !
                   @
         #

[7,8,9,0,1,2,3,4,5,6]
 !
                   @
         #

[5,6,7,8,9,0,1,2,3,4]
 !
                   @
         #
"""

"""
For problems related to Rotated Sorted Arrays, including this one and "33. Search in Rotated Sorted Array," the key is to categorize the cases to decide whether to narrow the search range to the left or
right of the current mid. Case categorization is the core of the logic.
"""
