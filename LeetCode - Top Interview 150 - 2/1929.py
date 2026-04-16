class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(2 * len(nums))]

        for index, num in enumerate(nums):
            result[index] = num
            result[index + len(nums)] = num

        return result
