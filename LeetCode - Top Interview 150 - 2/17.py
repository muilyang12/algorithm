"""
Slicing the array with digits[1:] and using a digits_left parameter was a poor choice. It would have been much better to use an index-based approach with a pointer instead.
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs_get_combination(target_index, result):
            if target_index == len(digits):
                return result

            new_result = []
            for r in result:
                for char in mapper[digits[target_index]]:
                    new_result.append(r + char)

            return dfs_get_combination(target_index + 1, new_result)

        return dfs_get_combination(0, [""])


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char_mapper = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(nums_left, combs):
            if len(nums_left) == 0:
                return combs

            target_num = nums_left[0]

            combs_new = []
            for comb in combs:
                for char in num_char_mapper[target_num]:
                    combs_new.append(comb + char)

            return dfs(nums_left[1:], combs_new)

        return dfs(digits, [""])


"""
digits = "23"

dfs(nums_left, combination)

[]

"2"
["a", "b", "c"]

"34" 
for current in []:
    for char in mapper[]

"a" + "d"
"a" + "e"
"a" + "f"

["ad", "ae", ...]

"4"
"""

"""
I found it relatively easy to write the DFS logic, but I was struggling with how to extract the final result array from the deepest level to the top.
"""
