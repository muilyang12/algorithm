"""
num1 = "123"
          ^
num2 = "456"
         ^

3 * 6 = 1, 8 (index = 0, 0)
3 * 5 = 1, 5 (index = 0, 1)
3 * 4 = 1, 2 (index = 0, 2)

[0,0,1,3,6,8]
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # digit_nums = [0 for _ in range(len(num1) + len(num2))]

        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
