"""
This problem definitely requires memorizing the specific algorithm. The basic idea is to start from 2 and eliminate all multiples of k, such as 2 * 2, 2 * 3, 2 * 4, and so on,
as long as they are less than n. A crucial detail is determining the upper limit for this process, which only needs to go up to n**0.5. The reasoning behind this is that any
composite number greater than n**0.5 must have at least one factor that is less than or equal to n**0.5, meaning those multiples would have already been cleared out during the
earlier stages of the process.
"""


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
