"""
This problem was quite difficult for me.

The core idea is that when you encounter a value smaller than the top of the stack you pop it and calculate the rectangle area. I did not fully understand this when I first
saw Gemini explanation so I watched NeetCode solution. Now I clearly understand why this is considered such a great problem.

Consider the sequence [1 2 3 4 2 ...]. You keep pushing into the stack until you reach 4. From the perspective of 1 2 3 and 4 they can still potentially extend their rectangles
to the right because the next value might be larger. However when the next value is 2 height 4 can no longer extend to the right. Its maximum width is now determined to be 1
so you can pop it and calculate the area. Similarly for height 3 since the new value is smaller than 3 the rectangle of height 3 can no longer grow to the right. Its maximum
width is fixed at 2 so you can pop and calculate. On the other hand the second 2 is not yet determined so it stays in the stack. In short you pop heights whose widths have been
finalized.

Also it is better to store indices in the stack for this problem. This makes it much easier to calculate the width quickly. It seems very common to store indices instead of
values in a stack or an array. When you need to consider the interval or distance rather than just the value itself looking at indices is the right way to go. This was also
true for problems like "739. Daily Temperatures" and "239. Sliding Window Maximum".

This truly is a great problem!
"""

"""
I thought I had a good grasp of this while taking notes but I guess it wasn't enough because I struggled a lot while actually solving the problem.

[2,1,7,4,6,5,3]

[2]
[1]
[1,7]
[1,4]
[1,4,6]
[1,4,5]
[1,3]

When 4 is popped and 3 is about to be pushed you must calculate the width of 4 using the current index 6 and the new stack top index 1 which results in 6 - 1 - 1. This is because
you need to consider both directions which are the distance to the first element smaller than the height to the right (from 4 to 5) and the distance to the first element smaller
than the height to the left (from 4 to 7).
"""

"""
[2,1,5,4,2,3]

stack = [1, 2, 3], 3

result = 8

=====

[4,2,0,3,2,5]

stack = [0, 2, 5], 5

result = 4
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0

        stack = []

        current = 0

        while current < len(heights):
            if not stack or heights[current] >= heights[stack[-1]]:
                stack.append(current)

                current += 1
            else:
                top_index = stack.pop()
                width = (current - stack[-1] - 1) if stack else current
                result = max(result, heights[top_index] * width)

        while stack:
            top_index = stack.pop()
            width = (len(heights) - stack[-1] - 1) if stack else len(heights)
            result = max(result, heights[top_index] * width)

        return result


"""
이 문제 보니까 "5. Longest Palindromic Substring" 문제가 떠오르네. 이 문제를 풀 때 i를 순회시키고 radius를 증가시키는 방식으로 했었지. O(n^2)의 시간 복잡도를 갖는 풀이이지. 이 문제의 경우도 비슷한 방식은 가능할 거 같네.

그런데 이 문제의 경우 가장 추천되는 방식은 Stack을 활용한 풀이이고 그 경우 O(n log n)의 시간 복잡도로 해결할 수 있을 거라고 하더라.
"""
