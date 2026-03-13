class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntegerMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        for index, char in enumerate(s):
            if char == "I" and index + 1 < len(s) and s[index + 1] in ["V", "X"]:
                result -= romanToIntegerMap["I"]

            elif char == "X" and index + 1 < len(s) and s[index + 1] in ["L", "C"]:
                result -= romanToIntegerMap["X"]

            elif char == "C" and index + 1 < len(s) and s[index + 1] in ["D", "M"]:
                result -= romanToIntegerMap["C"]

            else:
                result += romanToIntegerMap[char]

        return result


"""
M, D, L, V => Changed to its own number

I, X, C => if

III
1 1 1

MCMXCIV
1000 -100 1000 -10 100 -1 10
"""
