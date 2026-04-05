class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        memo = [0 for i in range(n + 1)]
        memo[0] = 0
        memo[1] = 1

        gap = 2

        for i in range(2, n + 1):
            if i >= gap * 2:
                gap *= 2

            memo[i] = memo[i - gap] + 1

        return memo


"""
n = 5

0 000
1 001
2 010
3 011
4 100
5 101

memo = [0, 1]

i 2 to n

memo[i] = memo[i - gap]

gap = 2
gap *= 2
"""

"""
I think this is a truly excellent problem. It focuses on Dynamic Programming as the main concept while also testing your understanding of Bit Manipulation.

However, I noticed that I keep using the exponentiation operator like memo[i] = memo[i - 2 ** current] + 1. Think about it, would it be okay to perform an exponentiation operation
every single time? The best approach is to use a gap variable and update it with *gap = 2. At the very least, you should ensure that the exponentiation happens only once, such as
setting gap = 2 ** current before entering the loop.
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        memo = [0 for i in range(n + 1)]
        memo[0] = 0
        memo[1] = 1

        current = 0
        for i in range(2, n + 1):
            if i >= 2 ** (current + 1):
                current += 1

            memo[i] = memo[i - 2**current] + 1

        return memo


"""
Bit Manipulation 문제의 경우 time complexity 계산이 조금 어려운 거 같아. for loop에서 n이 나오지. 그리고 저 while의 경우는 target이 계속 절반씩 줄어드는 거니가 log target 인거잖아. 즉 O(n log n) 이 되는 거지.
"""


# Time Complexity: O(n log n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            if i % 2 == 1:
                result.append(result[-1] + 1)
                continue

            count = 0

            target = i

            while target > 0:
                count += target % 2
                target >>= 1

            result.append(count)

        return result
