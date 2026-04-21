"""
1 => 1, 0 => Good
25 => 25, 0 => Good
26 => 0, 1 => Not Good (Should be 26, 0)
52 => 0, 2 => Not Good (Should be 26, 1)

When looking at individual cases like this, it seems you only need to worry about multiples of 26. For all other cases, standard `% 26` and `// 26` operations are sufficient without needing tricks like
subtracting 1. Honestly, laying out the cases one by one and analyzing them is a much more intuitive way to approach the problem.
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        current = columnNumber

        while current > 0:
            if current % 26 != 0:
                current_digit = current % 26
                current = current // 26
            else:
                current_digit = 26
                current = current // 26 - 1

            result = chr(current_digit + ord("A") - 1) + result

        return result


"""
This problem felt familiar, but the specific idea didn't come to mind until I talked with Gemini. It's essentially a base conversion concept, specifically base-26.

The core of the problem lies in breaking down a number into the form a * 26^n + b * 26^(n-1) + ...

Think about how you calculate the sum of digits in a base-10 number. You used the % 10 operation to get the digit and then //= 10 to move to the next. You fill in the digits starting from the right. The same
principle applies here. In any base-related problem, you must remember to fill in the values from the ones place using the % n operation.

"진법" is called base in English. "2진법" is Binary or base-2, "10진법" is Decimal or base-10, "16진법" is Hexadecimal or base-16, and "26진법" is Hexavigesimal or base-26.
"""

"""
There is one more trick to this problem. While there is no doubt that this is a base-26 problem since there are 26 characters, a standard base-26 system should map characters to the 0-25 range. However, in this
problem, 'A' is 1 instead of 0, which creates a discrepancy.

If we want to shift the mapping so that A is 0 and Z is 25, we need to determine when to perform the -1 operation. By listing out examples, it becomes clear that we must subtract 1 in every cycle. Although this
is visible when listing cases, it might not feel intuitive at first.

26 => 0, 25 // -1 -> 0, 25
52 => 0, 25 // -1 -> 1, 25 // -1 -> 0, 25
78 => 1, 25
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        current = columnNumber

        while current > 0:
            current -= 1

            current_digit = current % 26

            result = chr(current_digit + ord("A")) + result

            current = current // 26

        return result
