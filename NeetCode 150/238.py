class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [num for num in nums]
        for i in range(1, len(prefix_product)):
            prefix_product[i] = prefix_product[i - 1] * nums[i]
        suffix_product = [num for num in nums]
        for i in range(1, len(suffix_product)):
            suffix_product[-i - 1] = suffix_product[-i] * nums[-i - 1]

        result = []
        for i in range(len(nums)):
            value = 1
            if i - 1 >= 0:
                value *= prefix_product[i - 1]
            if i + 1 < len(nums):
                value *= suffix_product[i + 1]

            result.append(value)

        return result
