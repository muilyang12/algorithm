class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        result = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            old_start, old_end = result[-1]
            new_start, new_end = sorted_intervals[i]

            if new_start <= old_end:
                result[-1][0] = old_start
                result[-1][1] = max(old_end, new_end)
            else:
                result.append(sorted_intervals[i])

        return result


"""
Sorted?
All positive?
"""

"""
[[1,3]]
  ^
[[1,3],[2,6],[8,10],[15,18]]
        ^
"""
