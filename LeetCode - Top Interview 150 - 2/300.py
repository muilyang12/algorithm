"""
The previous approach for this problem used nested for loops resulting in O(n^2) complexity. However since "354. Russian Doll Envelopes" requires an O(n log n) solution,
I solved this problem once again using Binary Search to achieve that same efficiency.

nums = [10,9,2,5,3,7,101,18]

[10]
[9]
[2]
[2, 5]
[2, 3]
[2, 3, 7]
[2, 3, 7, 101]
[2, 3, 7, 18]
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        incresing_ss = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > incresing_ss[-1]:
                incresing_ss.append(nums[i])
            else:
                left = 0
                right = len(incresing_ss) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if incresing_ss[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid - 1

                incresing_ss[left] = nums[i]

        return len(incresing_ss)


"""
9
2, 5
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo = [1 for len(nums)]
        # for i 0 to len - 1
        # for j 0 to i - 1
        # if i > j then max memo[i] = max(memo[i], memo[j] + 1)
        # result = max(memo)
        # Alternatively, you can continuously update the result variable at the same time you update the `memo`` array. result = max(result, memo[i])


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1 for _ in range(len(nums))]
        result = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)
                    result = max(result, memo[i])

        return result


"""
Positive numbers?
"""

"""
DP

[]

Array

i th value relies on i-1 th value.

a_{n} = a_{n-1} + ...
"""

"""
[10,9,2,5,3,7,101,18]
  1 1 1 1 1 1   1  1
    1 1 2 2 3   4  4
"""

"""
In this case, memo[i] represents the maximum length of an Increasing Subsequence that ends with the i-th element. In array-based DP, memo[i] often denotes a state where the current element is the last
element of the sequence. Let's keep this in mind.
"""

"""
The definition of DP[i] here is the maximum length of an increasing subsequence that ends with the i-th element. This is why a nested for-loop `for i, for j` is used. If `nums[j] < nums[i]`, then DP[i]
can potentially be updated to `DP[j] + 1`. By taking the maximum of these values, I determine the longest subsequence ending at that specific position.
"""
