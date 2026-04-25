"""
envelopes = [[5,4],[6,4],[8,1],[6,7],[2,3],[7,8],[7,5],[8,6],[9,6]]
envelopes = [[2,3],[5,4],[6,7],[6,4],[7,8],[7,5],[8,6],[8,1],[9,6]]

[3,4,7,4,8,5,6,1,6]

[3]
[3,4]
[3,4,7]
[3,4,7]
[3,4,7,8]
[3,4,5,8]
[3,4,5,6]

I just talked with Gemini and there is a limitation to this idea. The elements in the array are not always necessarily a valid sequence. For example if you have [3, 4, 5, 8]
where both 5 and 8 have a width of 7, it is not a possible case in reality. The reason we use this approach anyway is to prepare for future cases where an envelope with a
larger width might have a smaller height than 8. By doing this, we prevent those cases from being discarded due to the height constraint when they actually appear.

Therefore if the problem asks for the actual sequence of the longest envelopes you would unfortunately have to check if the array is valid every time.
"""

"""
However writing the O(n^2) DP code as shown below resulted in a Time Limit Exceeded error. After talking more with Gemini I learned that LIS problems can be solved in
O(n log n) by using Binary Search.

I actually went to the "300. Longest Increasing Subsequence" problem and implemented the O(n log n) solution using Binary Search. The key idea in that problem was managing
the subsequence array to maintain an increasing order.
"""

"""
[[2,3],[5,3],[5,5],[6,4],[6,7]]

[[2,3],[5,5],[6,7]]
"""


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        incresing_ss = [envelopes[0][1]]

        for i in range(1, len(envelopes)):
            if envelopes[i][1] > incresing_ss[-1]:
                incresing_ss.append(envelopes[i][1])
            else:
                left = 0
                right = len(incresing_ss) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if incresing_ss[mid] < envelopes[i][1]:
                        left = mid + 1
                    else:
                        right = mid - 1

                incresing_ss[left] = envelopes[i][1]

        return len(incresing_ss)


"""
This problem felt quite difficult so I talked with Gemini to figure out how to solve it.

It turns out this is a 2D version of the "300. Longest Increasing Subsequence". Even when comparing two values like width and height a 1D array for memo is sufficient just
like in that problem. I wrote the following O(n^2) logic which is the exact same DP logic used in the previous problem.
"""


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes)

        result = 1
        memo = [1 for i in range(len(envelopes))]

        for i in range(1, len(memo)):
            for j in range(i):
                if (
                    envelopes[j][0] < envelopes[i][0]
                    and envelopes[j][1] < envelopes[i][1]
                ):
                    memo[i] = max(memo[i], memo[j] + 1)
                    result = max(result, memo[i])

        return result
