class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [num for num in nums]

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + prefix[i]

        return prefix
