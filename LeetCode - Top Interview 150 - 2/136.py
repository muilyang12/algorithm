# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result


"""
This feels almost like something you just have to memorize.

a XOR a = 0
a XOR 0 = a

By continuously connecting the values using XOR, all elements that appear twice will cancel out to zero, leaving only the single unique value as the final result.
"""


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
