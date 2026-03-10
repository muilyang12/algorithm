class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if (mid - 1 < 0 or nums[mid] != nums[mid - 1]) and (mid + 1 >= len(nums) or nums[mid] != nums[mid + 1]):
                return nums[mid]

            if mid % 2 == 0:
                if nums[mid - 1] != nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid - 1] != nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1


"""
If I see the array, it looks sorted?
Can I assume it?
Can I assume only positive integer is in here?
Only Ingegers here?
"""

"""
Sorted => Binary Search

left, right, mid

[1,1,2,3,3,4,4,8,8]
     !
       @
     #

[1,1,3,3,5,8,8]
           !
         @
         #

[3,3,7]
     !
     @
     #

the very left == mid // mid % 2 == 0 -> Search left
the very left == mid // mid % 2 == 1 -> Search right
"""

"""
I think the hardest part is identifying that a problem can be solved with Binary Search. The core of BS is cutting 
the search range in half with each step. The real challenge lies in finding that boundary condition to decide whether 
to look at the left or the right side based on the mid value.
"""
