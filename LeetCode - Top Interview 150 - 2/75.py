"""
This problem is quite difficult, so it feels like the specific steps of the solution need to be memorized.

The basic idea is simple where you maintain three pointers named `left`, `current`, and `right`. If the current value is 0, you swap it with the `left` pointer, and if it is 2, you swap it
with the `right` pointer.

The most critical part is that you perform `current += 1` when the value is 0 or 1, but you do not do so when the value is 2. This is because when you swap with the `right` pointer, you are
bringing in a value from an unsorted portion of the array, so you cannot be certain of what that new value is yet. Therefore, you must process the same `current` once more. In contrast, when
you swap with the `left`, you can be sure the value you receive is either 0 or 1 because the `current` has already passed through that section. This is why you can safely move forward with
`current += 1` in that case. Since the current pointer does not increment every single time, you must use a while loop instead of a for loop.
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1

        current = 0

        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]

                left += 1
                current += 1
            elif nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]

                right -= 1
            else:
                current += 1


"""
nums = [0,0,1,1,2,2]
        !
        @
                  #

====

nums = [1,0,2]
        !
          @
          #

=====

nums = [1,0,2]
        !
          @
          #
"""
