# Time Complexity: O(n log n + n log k) = O(n log n), Space Complexity: O(k) = O(n) (k: Number of used rooms)
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        end_time_heap = []
        heapq.heappush(end_time_heap, sorted_intervals[0].end)

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i].start >= end_time_heap[0]:
                heapq.heappop(end_time_heap)
                heapq.heappush(end_time_heap, sorted_intervals[i].end)
            else:
                heapq.heappush(end_time_heap, sorted_intervals[i].end)

        return len(end_time_heap)


"""
However, the approach below has a significant limitation. In the worst-case scenario, it results in O(n^2) time complexity because the earliest ending meeting could consistently
be in the very last meeting room. Since the logic involves repeatedly searching for the minimum value, using a Min Heap should have been the obvious choice to speed things up.
"""


# Time Complexity: O(n log n + nk) = O(n^2), Space Complexity: O(k) = O(n) (k: Number of used rooms)
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        end_time_list = []
        end_time_list.append(sorted_intervals[0].end)

        for i in range(1, len(sorted_intervals)):
            added = False

            for j in range(len(end_time_list)):
                if sorted_intervals[i].start >= end_time_list[j]:
                    end_time_list[j] = sorted_intervals[i].end
                    added = True
                    break

            if not added:
                end_time_list.append(sorted_intervals[i].end)

        return len(end_time_list)


"""
Sorted?
"""

"""
The most important concept in this problem is that you must think based on the end time. A room only becomes available for someone else once the previous meeting's end time has
passed. While it seems like an obvious thought, focusing on the end time is actually the core idea that solves the problem.
"""
