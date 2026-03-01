LOWER_LIMIT = -(2**31)
UPPER_LIIMIT = 2**31 - 1


class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        digits = []

        current = abs(x)
        while abs(current) > 0:
            digits.append(current % 10)
            current -= digits[-1]
            current = current // 10

        result = 0
        for index, digit in enumerate(digits):
            if index == 0 and digit == 0:
                continue

            if (
                is_negative
                and digit > abs(LOWER_LIMIT) - result / 10 ** (len(digits) - 1 - index)
            ) or (
                not is_negative
                and digit > UPPER_LIIMIT - result / 10 ** (len(digits) - 1 - index)
            ):
                return 0

            result += digit * 10 ** (len(digits) - 1 - index)

        return -result if is_negative else result


"""
I want to assume like the range of number is fine here.

x = 123

123 % 10 = 3
(123 - 3) / 10 = 12 % 10 = 2

[3, 2, 1]

3 * 10^2 + 2 * 10^1 ...

=====
Edge

x = 0
x = 10
x = -10
"""

"""
The core logic was straightforward, but handling boundary checks was tricky. Comparing the result after calculation is problematic because an overflow would have already occurred by then. Therefore, I implemented a pre-check logic to validate the value during the assembly process.
"""
