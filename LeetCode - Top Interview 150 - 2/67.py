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
