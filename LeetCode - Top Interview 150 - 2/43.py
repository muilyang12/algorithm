"""
I learned this solution while talking with Gemini a long time ago and I still remember it.

The ideas in this problem are quite brilliant.
1. Remember to use current1 and current2 as pointers.
2. Remember that multiplying two 3-digit numbers results in a value less than 1000 * 1000 which is 1,000,000 so it will be a 6-digit number.
3. When multiplying `num1[current1]` and `num2[current2]` the ones digit of the product will be placed at `result[current1 + current2]`.
4. It is also good to temporarily store values in `result[current1 + current2 + 1]` instead of using a separate `carry`. You must remember to use += instead of = for the assignment to avoid overwriting values
from previous calculations when `current1` moves forward.
"""

"""
num1 = "123"
         ^
num2 = "456"
         ^

0, 0 => 3 * 6 = 1, 8
0, 1 => 3 * 5 = 1, 5
0, 2 => 3 * 4 = 1, 2
1, 0 => 2 * 6 = 1, 2
1, 1 => 2 * 5 = 1, 0

[8, 1]
[8, 6, 1]
[8, 6, 3, 1]
[8, 8, 4, 1]
[8, 8, 4, 2]
"""


# Time Complexity: O(nm)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        digits = [0] * (len(num1) + len(num2) + 1)

        for i in range(len(num1)):
            num_one = int(num1[len(num1) - 1 - i])

            for j in range(len(num2)):
                temp_number = num_one * int(num2[len(num2) - 1 - j]) + digits[i + j]

                digits[i + j] = temp_number % 10
                digits[i + j + 1] += temp_number // 10

        while digits and digits[-1] == 0:
            digits.pop()

        result = ""
        for i in range(len(digits) - 1, -1, -1):
            result += str(digits[i])

        return result
