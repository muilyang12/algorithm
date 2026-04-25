class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0

        left = 0
        right = 0

        change = 0
        while right < len(nums):
            if change <= k:
                if nums[right] == 0:
                    change += 1

                right += 1

            while change > k:
                if nums[left] == 0:
                    change -= 1

                left += 1

            result = max(result, right - left)

        return result
