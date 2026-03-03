class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        left = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                left = i
                break

        if left == -1:
            for i in range(len(nums) // 2):
                temp = nums[i]
                nums[i] = nums[len(nums) - 1 - i]
                nums[len(nums) - 1 - i] = temp

            return

        current_min = nums[left + 1]
        right = left + 1
        for i in range(left + 1, len(nums)):
            if nums[i] <= current_min and nums[i] > nums[left]:
                current_min = nums[i]
                right = i

        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

        for i in range((len(nums) - left - 1) // 2):
            temp = nums[left + 1 + i]
            nums[left + 1 + i] = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = temp


"""
1,3,5,4,2 -> 1,4,2,3,5
  !   @
1,4,5,3,2
    !   @

    !   @
    1
    5,3,2,1
    ! ! @ @
    2

1,2,3 -> 1,3,2
  ^

1,2,3,4,5 -> 1,2,3,5,4
      ^

1,3,2 -> 2,1,3
^

2,1,3 -> 2,3,1
  ^

2,3,1 -> 3,1,2
! @
3,2,1 => 3,1,2

2,3,1,3,3
    ! @
2,3,3,1,3

1,2,10,9,8
  !      @
1,8,10,9,2
1,8,2,9,10 OK
"""
