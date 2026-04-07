class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        d_e_queue = deque()

        for i in range(k - 1):
            while d_e_queue and nums[d_e_queue[-1]] < nums[i]:
                d_e_queue.pop()

            d_e_queue.append(i)

        for i in range(k - 1, len(nums)):
            if d_e_queue and i - k + 1 > d_e_queue[0]:
                d_e_queue.popleft()

            while d_e_queue and nums[d_e_queue[-1]] < nums[i]:
                d_e_queue.pop()

            d_e_queue.append(i)

            result.append(nums[d_e_queue[0]])

        return result


"""
The simplest approach is to find the maximum value among the k elements directly, but doing it that way would result in a time complexity of O(kn).

After talking with Gemini, it suggested using a double-ended queue. The core rule is that whenever a new value is about to enter the deque, you must pop() any values currently in the queue that are smaller than
the new one. This ensures that the deque always maintains its elements in descending order.

There is one more clever trick to this approach. Initially, I was putting the actual numbers into the deque, but that made it difficult to check whether it was time to remove a specific number during the main
for-loop. Gemini suggested storing the indices instead. (I was originally thinking about using a tuple like `(number, index)`, but using just the index is much cleaner.)

At first, I thought that iterating through the deque at every step $i$ would result in a time complexity of O(nk). However, it turns out that isn't the case. Since unnecessary numbers are constantly being removed,
the length of the deque doesn't actually stay at $k$. Because every number is processed exactly once throughout the entire execution, the time complexity is naturally O(n).

I need to remember this specific while loop `while d_e_queue and nums[d_e_queue[-1]] < nums[i]:`.
"""

"""
[1,3,-1,-3,5,3,6,7]

[6]

[3, 3, 5, 5, 6]
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        max_in_window = -math.inf
        max_index = None

        for i in range(k):
            if nums[i] > max_in_window:
                max_in_window = nums[i]
                max_index = i

        result.append(max_in_window)

        for i in range(1, len(nums) - k + 1):
            if max_index < i:
                max_in_window = -math.inf
                max_index = None

                for j in range(i, i + k):
                    if nums[j] > max_in_window:
                        max_in_window = nums[j]
                        max_index = j

            if nums[i + k - 1] >= max_in_window:
                max_in_window = nums[i + k - 1]
                max_index = i + k - 1

            result.append(max_in_window)

        return result
