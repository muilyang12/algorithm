class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid**2 <= x < (mid + 1) ** 2:
                return mid
            elif x == (mid + 1) ** 2:
                return mid + 1
            elif x < mid**2:
                right = mid - 1
            else:
                left = mid + 1

        return right


"""
I feel that this problem is quite similar to "875. Koko Eating Bananas." The similarity lies in the fact that we perform a Binary Search on the actual numbers themselves rather than
using indices. It is also important to remember the point about setting $x$ as the initial value for right.
"""
