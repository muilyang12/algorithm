class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        current = n

        while current > 1:
            if (current & 1) == 1:
                return False

            current >>= 1

        return True


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        current = n

        while current > 1:
            if current % 2 == 1:
                return False

            current = current // 2

        return True
