class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)

        result = []

        for num in nums2:
            if num in nums1_set:
                result.append(num)
                nums1_set.remove(num)

        return result
