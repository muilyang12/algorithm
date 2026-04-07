class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        digit_sum, digit_carry = x ^ y, (x & y) << 1

        while digit_carry:
            digit_sum, digit_carry = (
                digit_sum ^ digit_carry,
                (digit_sum & digit_carry) << 1,
            )

        return bin(digit_sum)[2:]


"""
Keep the usage of binary-related functions in mind.
1. bin(3) = "0b11"
2. int("11", 2) = 3

It is also important to note that the result of `a & b << 1` is different from `(a & b) << 1`. Since the shift operator has a higher precedence than the AND operator, writing it the first way will cause the 
computer to execute it as `a & (b << 1)`. I need to be very careful with this distinction.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        large_length = max(len(a), len(b))

        result = ""

        carry = 0
        for i in range(large_length):

            new_digit = ""

            if len(a) - 1 - i < 0:
                if carry == 1 and b[len(b) - 1 - i] == "1":
                    new_digit = "0"
                    carry = 1
                elif carry == 1:
                    new_digit = "1"
                    carry = 0
                elif b[len(b) - 1 - i] == "1":
                    new_digit = "1"
                    carry = 0
                else:
                    new_digit = "0"
                    carry = 0

            elif len(b) - 1 - i < 0:
                if carry == 1 and a[len(a) - 1 - i] == "1":
                    new_digit = "0"
                    carry = 1
                elif carry == 1:
                    new_digit = "1"
                    carry = 0
                elif a[len(a) - 1 - i] == "1":
                    new_digit = "1"
                    carry = 0
                else:
                    new_digit = "0"
                    carry = 0

            else:
                if a[len(a) - 1 - i] == "1" and b[len(b) - 1 - i] == "1":
                    new_digit = "0" if carry == 0 else "1"
                    carry = 1
                elif a[len(a) - 1 - i] == "1":
                    new_digit = "1" if carry == 0 else "0"
                    carry = 0 if carry == 0 else 1
                elif b[len(b) - 1 - i] == "1":
                    new_digit = "1" if carry == 0 else "0"
                    carry = 0 if carry == 0 else 1
                else:
                    new_digit = "0" if carry == 0 else "1"
                    carry = 0

            result = new_digit + result

        if carry == 1:
            result = "1" + result

        return result

"""
This problem is essentially the same as 66. Plus One. It also reminds me of a question I received during an interview with a company. 
I was asked to solve something like "111" + "19".
"""
