class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, num in enumerate(nums):
            hash[num] = index

        for index, num in enumerate(nums):
            if target - num in hash and hash[target - num] != index:
                return [index, hash[target - num]]

        return []


"""
nums = [2,7,11,15], target = 9

{
2: 0
7: 1
11: 2
15: 3
}

2, 7 (= 9 - 2)

[0, 1]
"""
