"""
What kind of characters can come?
"""


# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += len(string) + "@" + string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        current = 0
        count_pointer = 0

        while current < len(s):
            count_pointer = current

            while s[count_pointer] in "0123456789":
                count_pointer += 1
            
            count = int(s[current:count_pointer])
            
        # Will stop solving here.
