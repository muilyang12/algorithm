"""
This problem is quite interesting and relies on three crucial ideas.

1. Using a stack is the fundamental starting point for the solution.
2. Storing indices in the stack is an excellent approach because the result array is not filled in a linear order.
3. Calculating the distance by finding the difference between the current index and the index stored in the stack is also key.

This problem is identical to "503. Next Greater Element II" and shares significant methodological similarities with "239. Sliding Window Maximum." The way you maintain the deque
in descending order in the sliding window problem is very similar to how the stack is handled here. While the sliding window problem includes an additional step of removing
expired elements from the left, the core logic of popping from the right to maintain order makes these problems nearly the same.
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = [0]

        for i in range(1, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                target_index = stack.pop()
                result[target_index] = i - target_index

            stack.append(i)

        return result


"""
temperatures = [73,74,75,71,69,72,76,73]
                   !

stack = [2,5]

result = [1,1,0,2,1,0,0,0]

=====

temperatures = [89,62,70,58,47,47,46,76,100,70]
                                      !

stack = [0,2,3,4]

result = [0,1,0,0,3,2,1,0,0,0]
"""
