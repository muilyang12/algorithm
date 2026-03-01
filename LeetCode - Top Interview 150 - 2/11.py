class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        result = 0

        while left < right:
            current = (right - left) * min(height[left], height[right])

            result = max(result, current)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return result
