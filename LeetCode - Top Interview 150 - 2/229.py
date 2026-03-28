class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_1 = None
        count_1 = 0
        candidate_2 = None
        count_2 = 0

        for i in range(len(nums)):
            if candidate_1 == nums[i]:
                count_1 += 1
            elif candidate_2 == nums[i]:
                count_2 += 1
            elif candidate_1 != nums[i] and count_1 == 0:
                candidate_1 = nums[i]
                count_1 = 1
            elif candidate_2 != nums[i] and count_2 == 0:
                candidate_2 = nums[i]
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1

        counts = {candidate_1: 0, candidate_2: 0}
        for num in nums:
            if num != candidate_1 and num != candidate_2:
                continue

            counts[num] += 1

        result = []
        if candidate_1 != None and counts[candidate_1] > len(nums) // 3:
            result.append(candidate_1)
        if candidate_2 != None and counts[candidate_2] > len(nums) // 3:
            result.append(candidate_2)

        return result


"""
This problem can be solved quite easily if you simply approach it using a Hash Map. However, as we did with "169. Majority Element," we can reduce the space complexity to O(1) by
applying the Boyer-Moore Voting Algorithm.

The core idea is to use two sets of candidate and count variables this time.

There are a few key points to keep in mind for this approach.
1. For problems asking for elements that appear more than n/2 or n/3 times, the candidate and count method is a viable solution.
2. It is better to initialize the candidate values as `None` to avoid conflicts with valid input data.
3. When checking if a candidate exists, you should use `if candidate != None` instead of `if candidate` because values like 0 or an empty string "" are falsy in Python.
4. Since there might be cases where an element appears exactly n/2 or n/3 times, a final verification step is necessary to confirm that the counts are truly larger than the required
threshold. This means there is no particular advantage in terms of time complexity compared to the Hash Map approach.
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_counters = {}

        for num in nums:
            if num not in num_counters:
                num_counters[num] = 0

            num_counters[num] += 1

        result = []
        for num, count in num_counters.items():
            if count > len(nums) // 3:
                result.append(num)

        return result
