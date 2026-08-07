class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0

        sorted_intervals = sorted(intervals)

        result = 0

        left = 0
        right = 1

        while right < len(sorted_intervals):
            l_s, l_e = sorted_intervals[left]
            r_s, r_e = sorted_intervals[right]

            if l_e <= r_s:
                left = right
                right = right + 1
            elif l_e < r_e:
                result += 1

                right += 1
            else:
                result += 1

                left = right
                right = right + 1

        return result
