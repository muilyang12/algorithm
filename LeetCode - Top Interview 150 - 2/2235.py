"""
```
while digit_carry != 0:
    digit_sum, digit_carry = digit_sum ^ digit_carry, (digit_sum & digit_carry) << 1
```

In other languages the above bitwise logic covers both positive and negative numbers. However in Python the int type can grow infinitely so this logic alone cannot handle
negative numbers. Therefore you must force the values into a 32-bit representation.

Remember these three points.
1. Declare mask = 0xFFFFFFFF and use the & mask operation every time to limit the values to 32 bits.
2. If the result is less than or equal to 0x7FFFFFFF it is positive so you can return it as is but otherwise you must treat it as a negative number.
3. When treating it as a negative number the calculation is done using `~(digit_sum ^ mask)`.

Honestly, I can accept using & mask, but ^ mask feels a bit forced. Given that the interviewer knows I am using Python, I don't think this specific problem will come up.
I'll just focus on memorizing this pattern.
"""


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        mask = 0xFFFFFFFF

        digit_sum = (num1 ^ num2) & mask
        digit_carry = ((num1 & num2) << 1) & mask

        while digit_carry != 0:
            temp_digit_sum = (digit_sum ^ digit_carry) & mask
            temp_digit_carry = ((digit_sum & digit_carry) << 1) & mask

            digit_sum = temp_digit_sum
            digit_carry = temp_digit_carry

        if digit_sum < 0x7FFFFFFF:
            return digit_sum
        else:
            return ~(digit_sum ^ mask)


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
