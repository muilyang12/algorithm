class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        digits = []

        current = x
        while current > 0:
            digits.append(current % 10)
            current = current // 10

        for i in range(len(digits) // 2):
            if digits[i] != digits[len(digits) - 1 - i]:
                return False

        return True


"""
121

[1, 2, 1]
 ^     ^

current = 121
current % 10 -> append to the array
current -= ___
current /= 10

[1, 2, 1]

121
12
1
0
"""
