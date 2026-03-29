class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        result = []

        target = sorted_intervals[0]

        for i in range(1, len(sorted_intervals)):
            existing_start, existing_end = sorted_intervals[i]
            target_start, target_end = target

            if existing_end < target_start:
                result.append(sorted_intervals[i])
            elif target_end < existing_start:
                result.append(target)
                target = sorted_intervals[i]
            else:
                target = [
                    min(existing_start, target_start),
                    max(existing_end, target_end),
                ]

        if target:
            result.append(target)

        return result


"""
There are several key points to keep in mind for this problem.

1. I need to be very clear about the two objects whose `start` and `end` values I am comparing. In my previous solution, I compared `result[-1]` with `sorted_intervals[i]`. In this
new approach, I am comparing `target` with `sorted_intervals[i]`. The idea is to only push an interval into the result once its processing is completely finished, which I think is
a solid way of thinking.
2. In "57. Insert Interval," once the `target` is pushed into the `result`, there are no further overlaps, so you can simply slice and append the remaining intervals. However, in
this problem, even after pushing the `target` into the `result`, there could still be subsequent overlaps with the following intervals. Therefore, I must continuously update the
`target` using the current interval and keep moving forward until the end.
3. When classifying cases, it is best to list all possible scenarios first and then write the if statements accordingly. This ensures that every case is handled thoroughly without
missing any details.
"""

"""
When comparing two intervals, the possible cases are as follows.

[  ]
     [  ]

[  ]
  [  ]

  [  ]
[  ]

     [  ]
[  ]
"""


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
