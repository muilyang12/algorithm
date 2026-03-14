"""
There is a follow-up question asking if I can solve the problem in O(1) extra space complexity. I feel like this optimization might be a bit excessive, so I just want to explain the logic 
in words.

The idea is to reuse the output array `result` to store the prefix products first. Then, by iterating backward `for i in range(n - 1, -1, -1)`, you can complete the result array by multiplying 
each element by the cumulative suffix product. This way, you don't need any additional arrays except for the one required for the result.
"""

# Time Complexity: O(2n) = O(n) // Space Complexity: O(2n) = O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [0 for _ in nums]
        prefix_products[0] = 1
        suffix_products = [0 for _ in nums]
        suffix_products[-1] = 1

        for i in range(1, len(nums)):
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
            suffix_products[len(nums) - 1 - i] = (
                suffix_products[len(nums) - i] * nums[len(nums) - i]
            )

        result = []
        for i in range(len(nums)):
            result.append(prefix_products[i] * suffix_products[i])

        return result


"""
The easiest way to solve this problem would be using the division operation. However, since the problem explicitly requires solving it "Without using the division operation", so I should
find another way.

When I followed a YouTube solution previously, I used the approach below. Here, `left` represents the prefix product and `right` represents the suffix product. Creating prefix and suffix
arrays seems like the most standard way to solve this problem. (Since it's better to use more CS-oriented terminology, let's use the variable names prefix and suffix.)

const left = [];
const right = [];
"""

"""
This problem has a core idea that feels very much like DP. After discussing it with Gemini, I learned that Prefix Sum is actually a type of DP. You have to continuously accumulate the
multiplication results from the beginning, and since the previous results are used to calculate the subsequent ones, it is indeed DP!
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        whole_product = 1
        for num in nums:
            if num != 0:
                whole_product *= num
            else:
                zero_count += 1

        if zero_count == 0:
            result = [whole_product // n for n in nums]
        elif zero_count == 1:
            result = [0 if n != 0 else whole_product for n in nums]
        else:
            result = [0 for _ in nums]

        return result
