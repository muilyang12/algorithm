class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = -1
        for pile in piles:
            max_pile = max(max_pile, pile)

        if len(piles) == h:
            return max_pile

        left = 1
        right = max_pile

        result = math.inf

        while left <= right:
            mid = (left + right) // 2

            hours = self.get_hours_to_finish(piles, mid)

            if hours > h:
                left = mid + 1
            elif hours <= h:
                result = min(result, mid)
                right = mid - 1

        return result

    def get_hours_to_finish(self, piles, speed):
        result = 0

        for pile in piles:
            if pile <= speed:
                result += 1

            elif pile % speed == 0:
                result += pile / speed

            elif pile % speed > 0:
                result += pile // speed + 1

        return result


"""
max_pile

1 ~ max_pile

[F, F, T, ... F]

Output

O(NM) => N: Length, M: Maximum
=====

1, 2, 3, 4, ... max_pile
         ^

Kind of search

Binary Search
"""

"""
h >= len(piles)
"""

"""
piles = [30,11,23,4,20], h = 5

30

1, 15, 30
16, 23, 30
24, 27, 30
28, 29, 30
30, 30

2 + 1 + 2 + 1 + 2 = 8
2 + 1 + 1 + 1 + 1 = 6
2 + 1 + 1 + 1 + 1 = 6
2 + 1 + 1 + 1 + 1 = 6
"""

"""
One important thing is that the while loop condition in Binary Search must be left <= right, including the equal sign. I keep forgetting to include that equality check.
"""
