class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = {}
        for char in s1:
            if not char in counts:
                counts[char] = 0

            counts[char] += 1

        left = 0
        right = 0

        while right < len(s2):
            if right < left + len(s1):
                char = s2[right]
                if not char in counts:
                    counts[char] = 0
                counts[char] -= 1

                right += 1

            else:
                char = s2[left]
                if not char in counts:
                    counts[char] = 0
                counts[char] += 1

                char = s2[right]
                if not char in counts:
                    counts[char] = 0
                counts[char] -= 1

                left += 1
                right += 1

            if all(value == 0 for value in counts.values()):
                return True

        return False
