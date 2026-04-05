# Time Complexity: O(log n) or O(32) = O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        target = n

        while target > 0:
            count += target & 1

            target >>= 1

        return count


"""
Bit Manipulation problems are becoming quite interesting as I continue to study them. I have tried three different methods for this.

1. Using the `bin()` function and checking `if char == "1"`.
2. Using the `& 2**current` operation. Since 2**current is a number where only one bit is 1, you can count the number of 1s by iterating through a for-loop.
3. Using the `% 2` (or `& 1`) operation combined with the `>>` bitwise shift operator. If the `% 2` or `& 1` operation results in 1, it means the current first bit is 1.
You then repeatedly apply the >> shift operator to reduce the number until it becomes 0.

In practice, methods 2 and 3 follow the same logic. However, the `& 1` operation in method 3 is much better than the `& 2**i` operation in method 2.

It is said that the time complexity of this approach can be interpreted as either O(log n) or O(32) = O(1).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        target = n

        while target > 0:
            count += target % 2

            target >>= 1

        return count


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        current = 0

        while 2**current <= n:
            if n & 2**current > 0:
                result += 1

            current += 1

        return result


class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)

        count = 0
        for i in range(2, len(bin_n)):
            if bin_n[i] == "1":
                count += 1

        return count
