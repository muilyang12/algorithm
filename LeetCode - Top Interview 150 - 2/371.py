"""
This problem is logically identical to "2235. Add Two Integers".

There are four key points to remember.
1. You must declare a `mask = 0xFFFFFFFF` and use the `& mask` operation at each step to limit the values to 32 bits.
2. If the result is less than or equal to 0x7FFFFFFF, it is a positive number and can be returned as is. Otherwise, it must be treated as a negative number and converted
accordingly.
3. The conversion for negative numbers is handled using the formula `~(digit_sum ^ mask)`.
4. The actual calculation is performed through the logic of `sum = sum ^ carry` and `carry = (sum & carry) << 1` (Repeated until the carry becomes zero).
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        digit_sum, digit_carry = (a ^ b) & mask, ((a & b) << 1) & mask

        while digit_carry > 0:
            temp_digit_sum = (digit_sum ^ digit_carry) & mask
            temp_digit_carry = ((digit_sum & digit_carry) << 1) & mask

            digit_sum = temp_digit_sum
            digit_carry = temp_digit_carry

        return digit_sum if digit_sum < 0x7FFFFFFF else ~(digit_sum ^ mask)
