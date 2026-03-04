class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(current, o, c):
            if len(current) == 2 * n:
                result.append(current)

            if o > c:
                if o < n:
                    dfs(current + "(", o + 1, c)

                if c < n:
                    dfs(current + ")", o, c + 1)
            else:
                if o < n:
                    dfs(current + "(", o + 1, c)

        dfs("", 0, 0)

        return result


"""
N = 3

o "((("
c ")))"

  _ _ _ _ _ _

o
c

Backtracking

dfs(current, o, c):
    if o > c:
        dfs(current + "(", o + 1, c)
        dfs(current + ")", o, c + 1)
    else:
        dfs(current + "(", o + 1, c)
"""

"""
Writing a recursive, DFS-style function feels pretty intuitive since it's backtracking. But the real key seems to be figuring out how to bring that innermost result back up to the top.
"""