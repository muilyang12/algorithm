# Time Complexity: O(nm)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return  "0"

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
