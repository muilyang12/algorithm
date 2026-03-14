# Time Complexity: O(n + m)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for char in s:
            if char not in hash:
                hash[char] = 0

            hash[char] += 1

        for char in t:
            if char not in hash:
                return False

            hash[char] -= 1
            if hash[char] == 0:
                del hash[char]

        if len(hash) > 0:
            return False
        else:
            return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if "".join(sorted(s)) == "".join(sorted(t)):
            return True
        else:
            return False
