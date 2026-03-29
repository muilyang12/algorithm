class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []

        target = newInterval

        for i in range(len(intervals)):
            interval = intervals[i]
            existing_start, existing_end = interval
            target_start, target_end = target

            if existing_end < target_start:
                result.append(interval)
            elif target_end < existing_start:
                result.append(target)
                result.append(interval)

                target = None
                result = result + intervals[i + 1 :]

                break
            else:
                target = [
                    min(existing_start, target_start),
                    max(existing_end, target_end),
                ]

        if target:
            result.append(target)

        return result


"""
No overlap between intervals?
Sorted?
"""

"""
The reason this problem was difficult is that I tried to perform the merge while simultaneously keeping track of three different things: result, intervals[i], and newInterval. To make this
problem easier to solve, you can add a single rule: only push an interval into result once it is completely finished. By doing this, result is no longer something you need to constantly
monitor. Instead, you can proceed by comparing only the target and the current intervals[i].

Also, after discussing it with Gemini, a great suggestion was made. Once the target is inserted into the result, there is no need to continue iterating through the remaining intervals.
Since the problem guarantees that there are no overlaps within the original intervals, you can simply slice the rest of the intervals and append them to the result using the `+` operator,
like this: `result = result + intervals[i + 1:]`.
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

     [  ]
[  ]
"""


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        added_intervals = []

        added = False
        for interval in intervals:
            if newInterval[0] < interval[0] and not added:
                added_intervals.append(newInterval)
                added = True

            added_intervals.append(interval)
        
        if not added:
            added_intervals.append(newInterval)
            added = True

        result = []
        result.append(added_intervals[0])

        for i in range(1, len(added_intervals)):
            existing_start, existing_end = result[-1]
            new_start, new_end = added_intervals[i]

            if existing_end >= new_start:
                result[-1][1] = max(existing_end, new_end)
            else:
                result.append(added_intervals[i])

        return result
