class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left = 0
        # right = length - 1

        # result = -math.inf
        # while left < right:
        #     result = max(result, (r - l) * max()))

        #     if h[l] > h[r]:
        #         r -= 1
        #     else:
        #         l += 1


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
