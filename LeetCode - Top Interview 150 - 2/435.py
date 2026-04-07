"""
intervals sorted?

intervals = [[1,2],[1,3],[2,3],[3,4]]
                                !     @

higher end value -> removed

count = 1

first_end
second_start

Time Complexity: O(n log n + n), Space Complexity: O(1)
"""


# Time Complexity: O(n log n + n) = O(n log n)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)

        result = 0

        first = 0
        second = 1

        while second < len(sorted_intervals):
            first_start, first_end = sorted_intervals[first]
            second_start, second_end = sorted_intervals[second]

            if first_end <= second_start:
                first = second
                second = first + 1
            elif first_end >= second_end:
                first = second
                second = first + 1
                result += 1
            else:
                second += 1
                result += 1

        return result


"""
[1, 2] [2, 4] -> Is this overlapping?
"""

"""
This problem is also quite challenging.

The idea seems quite clear. The goal is to determine if there is an overlap, and if so, one of the two intervals must be removed from the list. When choosing which of the two to remove,
the one with the later end time should be discarded. This is because the interval with an earlier end time is less likely to affect subsequent intervals. The most important point is to
focus on the end time rather than the duration of the interval.
"""

"""
It seems like there are two main types of interval problems. Those where you need to merge intervals and those where you need to avoid overlaps between them.

1. In problems involving merging intervals, the most important factor is clearly identifying the two targets for comparison.
2. On the other hand, in problems where you must avoid overlaps, focusing on the end time is the key.
"""
