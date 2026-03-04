class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        result = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue

            current = num
            current_length = 0
            while current in nums_set:
                current += 1
                current_length += 1

            result = max(result, current_length)

        return result


"""
nums = [100,4,200,1,3,2]
nums_set = {100,4,200,1,3,2}

{100, 200, 1}

for num in nums:
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        starts = []
        for num in nums_set:
            if num - 1 not in nums_set:
                starts.append(num)

        result_length = 0
        for start in starts:
            current = start
            current_length = 0
            while current in nums_set:
                current_length += 1
                current += 1
            
            result_length = max(result_length, current_length)

        return result_length


"""
Combining two for-loop into a single for-loop is a clever approach. The core idea here is definitely identifying the start or end point.
"""