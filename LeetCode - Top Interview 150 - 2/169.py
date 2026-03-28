# Boyer-Moore Voting Algorithm
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            elif nums[i] != candidate and count == 0:
                candidate = nums[i]
                count = 1
            else:
                count -= 1

        return candidate


"""
If you solve this using a Hash Map, you can achieve $O(n)$ for both space and time complexity, but that approach felt a bit too straightforward. After discussing it with Gemini, I learned
that there is a famous follow-up for this problem to optimize the space complexity to $O(1)$. Honestly, I wonder if this approach relies too heavily on a specific, clever idea.

The method is called the Boyer-Moore Voting Algorithm. The core idea involves using two variables, `candidate` and `count`. Whenever the count is zero, you set the `candidate` to the current
number. If the next number is the same as the current `candidate`, you increment the `count`. If it is different, you decrement the `count` by one. You simply repeat this process throughout
the array.
"""


# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counters = {}

        for num in nums:
            if num not in num_counters:
                num_counters[num] = 0

            num_counters[num] += 1

        result = -1
        max_count = -math.inf
        for num, count in num_counters.items():
            if count > max_count:
                result = num
                max_count = count

        return result
