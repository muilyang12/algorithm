"""
문제를 아래처럼 푼 후 Gemini랑 대화를 좀 했지. Gemini는 그 소리를 하더라고. prefix_sum을 배열로 갖지 않으면서 해보자고 말이야. 그치 사실상 아래 방식에서 풀면 약간 불필요하게 두 바퀴 도는 느낌이야. 각 인덱스별로 현재까지의 sum을 구해서 배열에 넣고 후처리 없이 다음 for loop에서 바로 다시 도는 거니까 말이야.
"""


# Time Complexity: O(2n) = O(n), Space Complexity: O(2n) = O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0 for _ in nums]
        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        result = 0

        hash = {0: [-1]}
        for index, prefix in enumerate(prefix_sum):
            if prefix - k in hash:
                result += len(hash[prefix - k])

            if prefix not in hash:
                hash[prefix] = []

            hash[prefix].append(index)

        return result


"""
Problems asking for the sum of a subarray can generally be solved in two ways.

First, there is the Sliding Window approach. To use a Sliding Window, the changes that occur when expanding the right side or shrinking the left side must be predictable. Because of this,
it typically requires conditions such as having only positive numbers or a sorted array.

Second, there is the Prefix Sum approach. While this increases the space complexity to $O(n)$, it has the advantage of not requiring any specific conditions on the values within the array,
unlike the Sliding Window method.
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {}
        hash[0] = [-1]

        result = 0

        current_sum = 0
        for index, num in enumerate(nums):
            current_sum += num
            if current_sum not in hash:
                hash[current_sum] = []

            if current_sum - k in hash:
                result += len(hash[current_sum - k])

            hash[current_sum].append(index)

        return result


"""
Should be contiguous?
All elements selected should be originally next to each other?
All numbers should be positive?
Negative can come?
Sorted?
"""

"""
Whenever I encounter problems involving subsequences, substrings, ors ubarrays, I must always ask about continuity. Keep this in mind!
"""

"""
Maybe it's because I've only solved this problem once. I missed the most crucial point. This problem cannot be solved using a Sliding Window. To use a Sliding Window for sums, you either need a sorted array or strictly positive values. That way, removing a value from the left and adding one to the right produces a consistent, predictable result. But since this problem has neither sorting nor exclusively positive numbers, Sliding Window is not an option.
"""

"""
The logic here is genius. Since the sum of a `subarray [i, j]` can be calculated as `prefixSum[j] - prefixSum[i-1]`, we can leverage this to solve the problem efficiently. What a great approach!
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)

        result = 0

        for i in range(len(nums)):
            temp_sum = 0
            for j in range(i, len(nums)):
                temp_sum += nums[j]

                if temp_sum == k:
                    result += 1

        return result