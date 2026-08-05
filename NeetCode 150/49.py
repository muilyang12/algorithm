class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if not sorted_string in hash:
                hash[sorted_string] = []

            hash[sorted_string].append(string)

        result = []
        for value in hash.values():
            result.append(value)

        return result
