class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0

        result = [1] * n

        result[0] = 0
        result[1] = 0

        for i in range(2, int(n**0.5) + 1):
            if result[i] == 0:
                continue

            current = 2

            while current * i < n:
                result[current * i] = 0

                current += 1

        return sum(result)


"""
100 -> 10

11 * 2
11 * 3
11 * 4
11 * 5
11 * 6
11 * 7
13 * 3
25 * 8
"""
