"""
The easiest way is to use slicing to create rotated_nums and then move the values. In this case, you can solve the problem with $O(n)$ time and $O(n)$ space complexity.

There is also a method involving three reversals. [1,2,3,4,5,6,7] -> [1,2,3,4,7,6,5] -> [4,3,2,1,7,6,5] -> [5,6,7,1,2,3,4] This approach allows you to solve it with O(2n) = O(n) time complexity and O(1) space complexity.
But honestly, it feels like one of those solutions you just have to memorize.
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_array(start, end):
            for i in range((end - start + 1) // 2):
                temp = nums[start + i]
                nums[start + i] = nums[end - i]
                nums[end - i] = temp

        k = k % len(nums)

        reverse_array(len(nums) - k, len(nums) - 1)
        reverse_array(0, len(nums) - k - 1)
        reverse_array(0, len(nums) - 1)
