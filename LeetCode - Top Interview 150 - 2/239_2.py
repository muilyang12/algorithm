class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        d_e_queue = deque()

        current = 0
        while current < len(nums):
            while d_e_queue and nums[d_e_queue[-1]] < nums[current]:
                d_e_queue.pop()

            d_e_queue.append(current)

            if d_e_queue and current - d_e_queue[0] >= k:
                d_e_queue.popleft()

            if current >= k - 1:
                result.append(nums[d_e_queue[0]])

            current += 1

        return result


"""
nums = [1,3,-1,-3,5,3,6,7]
                !   @

3, 3, 5, 5

O(kn)

=====

nums = [1,3,-1,-3,5,3,6,7]
        ^
d_e_queue = [1]
"""
