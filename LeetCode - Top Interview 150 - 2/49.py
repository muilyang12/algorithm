# Time Complexity: O(n * mlogm)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for string in strs:
            sorted_str = "".join(sorted(string))

            if sorted_str not in hash:
                hash[sorted_str] = []

            hash[sorted_str].append(string)

        return list(hash.values())

# Time Complexity: O(nm) (m: length of each string)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for string in strs:
            counts_tuple = self.get_counts_tuple(string)

            if counts_tuple not in hash:
                hash[counts_tuple] = []

            hash[counts_tuple].append(string)

        return list(hash.values())

    def get_counts_tuple(self, str):
        char_counts = {}
        for char in str:
            if char not in char_counts:
                char_counts[char] = 0

            char_counts[char] += 1

        keys = sorted(list(char_counts.keys()))

        return tuple((k, char_counts[k]) for k in keys)

"""
[(k, char_counts[k]) for k in keys]
((k, char_counts[k]) for k in keys)

These two are completely different. Since the former creates a list, I thought the latter would naturally create a tuple. However, the result was different. Through my conversation with Gemini, I learned
that the latter is a Python syntax called a Generator Expression.

gen_exp = (x**2 for x in range(10))
sum(gen_exp)

Or

sum(x**2 for x in range(10))

I've actually seen that second pattern a few times before.
"""

"""
Using `"".join(sorted())` results in a time complexity of O(m log m) due to the sorting process. On the other hand, creating a hash to count the frequency of each character has a time complexity of O(m).
Therefore, if the strings were longer, the latter method would be faster. However, in this case, the sorting method actually performed better. This is likely because, for shorter strings, the constant-time
overhead of the O(m) approach outweighs the theoretical efficiency gain.

Regardless, I must remember the core idea regarding Anagrams. If two strings are anagrams, they will yield the same result when their characters are sorted!
"""
