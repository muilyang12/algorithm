class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        target_indice = set()
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 0:
            target_indice.add(total_len // 2 - 1)
            target_indice.add(total_len // 2)
        else:
            target_indice.add(total_len // 2)

        left = 0
        right = 0
        total_index = 0

        result = 0

        while total_index < total_len:
            if (left < len(nums1) and right >= len(nums2)) or (
                left < len(nums1) and right < len(nums2) and nums1[left] <= nums2[right]
            ):
                if total_index in target_indice:
                    result += nums1[left]

                left += 1

            elif (right < len(nums2) and left >= len(nums1)) or (
                left < len(nums1) and right < len(nums2) and nums2[right] < nums1[left]
            ):
                if total_index in target_indice:
                    result += nums2[right]

                right += 1

            total_index = left + right

        return result / len(target_indice)


"""
len(nums1) len(nums2)

nums1 = [1,2], nums2 = [3,4]

4 => 2nd and 3rd

left = 0
right = 0

[1,2]
     ^

[3,4]
     ^

[1, 2]

2
2
4
"""
