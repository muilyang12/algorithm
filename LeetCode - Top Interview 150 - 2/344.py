class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[-1 - i]
            s[-1 - i] = temp
