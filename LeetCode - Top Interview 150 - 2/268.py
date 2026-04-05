class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        for i in range(len(nums) + 1):
            result ^= i

        return result


"""
To be honest, you can solve this by calculating sum(0 to n) - sum(nums) = Missing Number, which also achieves O(n) time complexity and O(1) space complexity.

If you consider the range from 0 to $n$ and the given nums together, only one number appears once while all others appear twice. In other words, it is essentially the same problem
as "136. Single Number".

3 11
0 00
1 01
^ 10

0 00
1 01
2 10
3 11
^ 00
"""
