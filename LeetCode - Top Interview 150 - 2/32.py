"""
It seems like this problem can be implemented in several ways. First it can be solved using a Stack. Since it is a valid parenthesis problem it is natural to use a stack.

Initially I tried to calculate the width using the popped index or the index at `stack[-1]` after a pop operation just like the approach used in "84. Largest Rectangle in Histogram". However there was an issue
where it would return 6 for an example like `()(()())` by only picking `(()())` and excluding the preceding `()`. For this problem you can supplement the solution by including a variable like `start_point` and
setting it this way. You can simply consider that a valid parenthesis pair starts from that specific point. You start with 0 and update it to i + 1 upon failure.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        stack = []

        start_point = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()

                    temp_result = i - stack[-1] if stack else i - start_point + 1
                    result = max(result, temp_result)
                else:
                    start_point = i + 1
                    continue

        return result


"""
s = ")()())"

[]
"""

"""
I recently solved "678. Valid Parenthesis String" which included the wildcard character *. In that problem I used a method of counting open parentheses with min_open_count and max_open_count. Having solved
that recently this counting approach came to mind for the current problem as well.

However when using this Sliding Window approach I realized there is a problem. While it can handle cases with too many closing parentheses it fails when there are too many opening parentheses. For example
with `(()` it ends with left = 0 and right = 2 but since open_count never reaches 0 the result is not updated.

After discussing this with Gemini it suggested going in both directions. Moving from back to front can handle the case with too many opening parentheses but it will have limitations with too many closing
parentheses. The two results will complement each other. This feels somewhat similar to how I used two-way memoization in "238. Product of Array Except Self".

I finished the implementation since I started it but I think using a Stack is a better way to solve this problem.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result_left = 0
        open_count_left = 0

        left_left = 0
        right_left = 0

        result_right = 0
        close_count_right = 0

        left_right = len(s) - 1
        right_right = len(s) - 1

        while right_left < len(s):
            if s[right_left] == "(":
                open_count_left += 1
            else:
                open_count_left -= 1

            if open_count_left < 0:
                left_left = right_left + 1
                right_left = left_left

                open_count_left = 0
            elif open_count_left > 0:
                right_left += 1
            elif open_count_left == 0:
                result_left = max(result_left, right_left - left_left + 1)
                right_left += 1

        while left_right >= 0:
            if s[left_right] == ")":
                close_count_right += 1
            else:
                close_count_right -= 1

            if close_count_right < 0:
                right_right = left_right - 1
                left_right = right_right

                close_count_right = 0
            elif close_count_right > 0:
                left_right -= 1
            elif close_count_right == 0:
                result_right = max(result_right, right_right - left_right + 1)
                left_right -= 1

        return max(result_left, result_right)


"""
s = ")()())"
      !
          @

left, right

open_count >= 0

open_count = -1

result = 4
"""
