class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]

        result = 0

        while left < right:
            if max_left <= max_right:
                left += 1

                max_left = max(max_left, height[left])
                result += max(min(max_left, max_right) - height[left], 0)
            else:
                right -= 1

                max_right = max(max_right, height[right])
                result += max(min(max_left, max_right) - height[right], 0)

        return result


"""
[0,1,0,2,1,0,1,3,2,1,2,1]
               ! @

3, 2

+1 +1 +2 +1
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0 for _ in height]
        max_left[0] = height[0]
        max_right = [0 for _ in height]
        max_right[-1] = height[-1]

        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i - 1])
            max_right[-1 - i] = max(height[-1 - i], max_right[-i])

        result = 0
        for i in range(1, len(height) - 1):
            result += max(0, min(max_left[i], max_right[i]) - height[i])

        return result


"""
[0,1,0,2,1,0,1,3,2,1,2,1]
               ! @

3, 2

+1 +1 +2 +1
"""
