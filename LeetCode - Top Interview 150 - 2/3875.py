class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_count = 0
        even_count = 0

        for index, num in enumerate(nums1):
            if num % 2 == 1:
                odd_count += 1
            else:
                even_count += 1

        all_odd_possible = True if even_count == 0 or odd_count > 0 else False
        all_even_possible = True if odd_count == 0 or odd_count > 1 else False

        return all_odd_possible or all_even_possible


"""
[2, 3]

[2, 2, 4]
"""
