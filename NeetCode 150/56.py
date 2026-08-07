class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)

        result = []
        target = sorted_intervals[0]

        for i in range(1, len(sorted_intervals)):
            t_l, t_r = target
            c_l, c_r = sorted_intervals[i]

            if t_r < c_l:
                result.append(target)
                target = sorted_intervals[i]

            else:
                target = [t_l, max(t_r, c_r)]

        result.append(target)

        return result
