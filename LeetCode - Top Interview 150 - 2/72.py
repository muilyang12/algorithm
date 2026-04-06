"""
The 2D DP problems involving strings, like "1143. Longest Common Subsequence", "72. Edit Distance", and "115. Distinct Subsequences" are truly challenging.

In "1143. Longest Common Subsequence", the values for `memo[i][0]` were simply 0, so I didn't need to worry too much about the initial values. However, in "72. Edit Distance" the value for `memo[i][0]` must be `i`
because it takes i deletions to match. This means I really need to be careful about setting the initial values in this case.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0 for _ in range(len(word2) + 1)] for __ in range(len(word1) + 1)]
        for i in range(len(memo)):
            memo[i][0] = i
        for j in range(len(memo[0])):
            memo[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    insert = memo[i - 1][j] + 1
                    delete = memo[i][j - 1] + 1
                    replace = memo[i - 1][j - 1] + 1
                    memo[i][j] = min(insert, delete, replace)

        return memo[-1][-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for __ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i

        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = dp[i][j - 1] + 1
                    delete = dp[i - 1][j] + 1
                    replace = dp[i - 1][j - 1] + 1

                    dp[i][j] = min(insert, delete, replace)

        return dp[len(word1)][len(word2)]


"""
"horse"
"ros"

[0,1,2,3]
[1,0,0,0]
[2,0,0,0]
[3,0,0,0]
[4,0,0,0]
[5,0,0,0]

dp[1][1] = 1
dp[1][2] = 1
"""


"""
The core of any DP problem is defining the state, such as DP[i] or DP[i][j]. In this case, it was clear that the result for i would depend on i-1, but it was particularly difficult to figure out what DP[i][j] should actually represent.

Let's define DP[i][j] as the minimum number of operations required to convert the first i characters of word1 into the first j characters of word2. With this definition, if we add one character to both and they match, the DP value remains the same. If they are different, we add +1 to account for a Replace operation.

Even after finding the definition of DP[i][j], the problem is still tough. What if the additional operation performed this time is a Replace? What if it's a Delete? Or an Insert? We need to calculate each of these three cases and update the DP table by finding the minimum value.

Replace: Assuming we know DP[i-1][j-1], we can get DP[i][j] by simply adding 1 to replace the newly added character.
Delete: Assuming we know DP[i-1][j], we already know how to make j characters with i-1. So, we just delete the i-th character (+1) to get DP[i][j].
Insert: Assuming we know DP[i][j-1], we already know how to make j-1 characters with i. So, we just add the j-th character (+1) to get DP[i][j].
"""
