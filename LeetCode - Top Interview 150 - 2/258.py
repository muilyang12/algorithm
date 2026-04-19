class Solution:
    def addDigits(self, num: int) -> int:
        def dfs_add_digits(num):
            if num < 10:
                return num

            result = 0
            current = num
            while current > 0:
                result += current % 10
                current //= 10

            return dfs_add_digits(result)

        return dfs_add_digits(num)


"""
This problem was easy to solve since it deals with decimal digits, which I have practiced many times, but I wanted to revisit it because I struggled a bit with the base-26
system in "168. Excel Sheet Column Title." It is crucial to remember that in number base conversion problems, you must always fill in the digits starting from the ones place.
"""
