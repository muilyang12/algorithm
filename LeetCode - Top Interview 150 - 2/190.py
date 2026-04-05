class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        target = n

        # while target > 0:
        for _ in range(32):
            result <<= 1

            result |= target & 1

            target >>= 1

        return result


"""
This problem presents an excellent idea. You extract the last bit from the original number and place it into the result number using an XOR or OR operation. Then, for every
`target >>= 1` operation applied to the original number, you apply `result <<= 1` operation to the result number. This is a very useful concept to remember.

Furthermore, you must use `for _ in range(32)` loop instead of `while target > 0` approach. If you use `while target > 0`, the loop terminates as soon as the original number
reaches zero (00000100 -> 0000010 -> 000001 -> 00000), failing to push the all zeros. Since the problem specifies a fixed 32-bit integer, you must complete exactly 32 iterations
to ensure all bits are correctly shifted.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        binary_n = bin(n)
        binary_n = binary_n[2:]
        binary_n = "".join(["0" for _ in range(32 - len(binary_n))]) + binary_n

        result = ""

        for i in range(len(binary_n) - 1, -1, -1):
            result += binary_n[i]

        return int(result, 2)
