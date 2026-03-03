class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0

        checked = set()
        while right < len(nums):
            if nums[right] not in checked:
                checked.add(nums[right])

                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

                left += 1
                right += 1
            else:
                right += 1

        return left


"""
[0,0,1,1,1,2,2,3,3,4]
     ^     ^

set(0,1,2,3)
[0,1,2,3,4,0,2,1,3,1]
           !
                     @

[0,1,2,3,4,_,_,_,_,_]
"""
