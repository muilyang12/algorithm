class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        starts = set()
        for num in nums:
            if num - 1 in nums_set:
                continue

            starts.add(num)

        result = 0
        for num in starts:
            current = num
            current_length = 0

            while current in nums_set:
                current_length += 1
                result = max(result, current_length)

                current += 1

        return result
