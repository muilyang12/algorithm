"""
The idea for this problem is truly excellent. You can solve it relatively easily by filling `nums1` from the back (Selecting the larger value between `nums1` and `nums2`).

However, you have to keep in mind that one side will inevitably finish first. Because of that, you must include two additional while loop at the end to handle any remaining elements.
"""

"""
nums1 = [1,2,3,0,0,0]
             ^   ^
nums2 = [2,5,6]
           ^

current1 = 2
current2 = 2
current_total = 5
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        current1 = m - 1
        current2 = n - 1
        current_total = m + n - 1

        while current1 > -1 and current2 > -1:
            if nums1[current1] >= nums2[current2]:
                nums1[current_total] = nums1[current1]

                current1 -= 1
                current_total -= 1
            else:
                nums1[current_total] = nums2[current2]

                current2 -= 1
                current_total -= 1

        while current1 > -1:
            nums1[current_total] = nums1[current1]

            current1 -= 1
            current_total -= 1

        while current2 > -1:
            nums1[current_total] = nums2[current2]

            current2 -= 1
            current_total -= 1
