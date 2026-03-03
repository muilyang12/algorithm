class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0

        while right < len(nums):
            if left == right and nums[left] != val:
                left += 1
                right += 1

            elif nums[left] == val and nums[right] == val:
                right += 1

            elif nums[left] != val and nums[right] != val:
                left += 1

            elif nums[left] == val and nums[right] != val:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

                left += 1
                right += 1

        return left


"""
[0,1,2,2,3,0,4,2]
     ^
         ^
[0,1,3,2,2,0,4,2]
       !
           @
[0,1,3,0,2,2,4,2]
         !
             @
[0,1,3,0,4,2,2,2]
           !
                 @
O(n)

=====

[0,1,2,2,3,0,4,2] val = 2
                 ^

Count of val => 3
[2,3,7]
target indice = [5,6]

O(n)
"""
