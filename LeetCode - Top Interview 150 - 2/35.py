class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return right + 1


"""
Sorted array

Find number or finde index

=> BS

nums = [1,3,5,6], target = 5

1,3,5,6
! #   @
    ! @
    #

return index of left

nums = [1,3,5,6], target = 4

1,3,5,6
! #   @
    ! @
    #
  @ !

If it can't find,

left => larger than target
left - 1 => smaller than target

nums = [1,3,5,6], target = 7

1,3,5,6
! #   @
    ! @
    #
      !
      @
      #
        !
      @
"""
