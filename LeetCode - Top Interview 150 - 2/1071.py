"""
The solution below is a bit disappointing. If you want to check for divisibility, you should first verify whether the length of the original string is a multiple of the divisor's
length. If they share a multiple relationship, you should then check if divisor * count == original. The approach of building a string using current += char is quite inefficient
compared to this method.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        current = ""
        index = 0

        while index < min(len(str1), len(str2)):
            if str1[index] != str2[index]:
                break

            current += str1[index]

            if self.is_divisor(str1, current) and self.is_divisor(str2, current):
                result = current

            index += 1

        return result

    def is_divisor(self, original, divisor):
        if len(original) % len(divisor) != 0:
            return False

        if divisor * (len(original) // len(divisor)) == original:
            return True
        else:
            return False


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        current = ""
        index = 0

        while index < min(len(str1), len(str2)):
            if str1[index] != str2[index]:
                break

            current += str1[index]

            if self.is_divisor(str1, current) and self.is_divisor(str2, current):
                result = current

            index += 1

        return result

    def is_divisor(self, original, divisor):
        if len(original) % len(divisor) != 0:
            return False

        result = ""

        while len(result) < len(original):
            result += divisor

        return result == original
