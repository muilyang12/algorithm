"""
It is a great coincidence that I solved two identical problems back to back.

This problem is perfectly identical to "739. Daily Temperatures" because it involves finding the nearest element to the right that is larger than the current one. The only difference
is the circular property of the array. To handle this, I can iterate through `i` up to twice the length of the array and use `i % length` to access the correct index for the values.
While using `array = array * 2 is possible`, the index-based approach is much better.

The logic for calculating `modified_i` is definitely something worth remembering.
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)

        stack = [0]

        for i in range(1, 2 * len(nums)):
            modified_i = i % len(nums)

            while stack and nums[stack[-1]] < nums[modified_i]:
                target_index = stack.pop()
                result[target_index] = nums[modified_i]

            stack.append(modified_i)

        return result


"""
0 ~ length - 1
length ~ 2 length - 1
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)

        stack = [0]

        for i in range(1, len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                target_index = stack.pop()
                result[target_index] = nums[i]

            stack.append(i)

        return result
