class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 1. memo0, memo1 = [0 for _], [0 for _]
        # 2. memo0[i] = max(memo0[i - 1] * nums[i], memo1[i - 1] * nums[i], nums[i])
        # 3. memo1[i] = min(...)
        # 4. result = max(result, memo0[i], memo1[i])
        # 5. The most critical point is that memo0 stores the maximum value while memo1 stores the minimum value.
        # 6. Also, you must include the current element, nums[i], when performing the updates.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]

        dp0 = [0 for _ in nums]
        dp0[0] = nums[0]
        dp1 = [0 for _ in nums]
        dp1[0] = nums[0]

        for i in range(1, len(nums)):
            dp0[i] = max(dp0[i - 1] * nums[i], dp1[i - 1] * nums[i], nums[i])
            dp1[i] = min(dp0[i - 1] * nums[i], dp1[i - 1] * nums[i], nums[i])

            result = max(result, dp0[i])
            result = max(result, dp1[i])

        return result


"""
This problem is definitely a tough one.

Initially, I approached it as a 2D DP problem where I defined DP[i][j] as the product from index i to j. I updated the DP array by multiplying the newly added j with the value at j - 1. However, this method
results in a time complexity of O(n^2) and a space complexity of O(n^2), which led to a "Memory Limit Exceeded" error. Getting a memory error like that is usually a clear sign that I should avoid using a 2D
DP approach.

After discussing it with Gemini, I found that a 1D DP approach is more than enough for this. Since we have to handle negative numbers, the suggestion was to create two arrays, dp1 and dp2, to represent the
maximum and minimum products of subarrays ending at index i. The idea is to compare dp1[i - 1] * nums[i] and dp2[i - 1] * nums[i].

However, there is one detail that is very easy to overlook. You must also consider nums[i] itself as a third option, which means starting a brand new subarray from the current position and ignoring the
previous products.
"""
