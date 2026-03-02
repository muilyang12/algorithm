class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for index in range(len(strs[0])):
            targetChar = strs[0][index]

            for string in strs:
                if index < len(string) and string[index] == targetChar:
                    continue
                else:
                    return result

            result += targetChar

        return result


"""
strs = ["flower","flow","flight"]

result = ""

for index in range(len(strs[0])):
    for i in range(len(strs)):

6
0 -> f
1 -> fl
2 -> break and retun fl
"""
