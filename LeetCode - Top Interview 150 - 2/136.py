class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set()

        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                nums_set.remove(num)

        if len(nums_set) == 1:
            return nums_set.pop()


"""
Only twice or once, right?
Eveything is number, right?
"""

"""
set()

{4}

[4,1,2,1,2]
"""
