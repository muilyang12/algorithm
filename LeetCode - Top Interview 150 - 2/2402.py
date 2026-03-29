class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        sorted_meetings = sorted(meetings)

        counts = {i: 0 for i in range(n)}

        unused_rooms_heap = [i for i in range(n)]
        heapq.heapify(unused_rooms_heap)

        timers_heap = []
        new_room_number = heapq.heappop(unused_rooms_heap)
        heapq.heappush(timers_heap, (sorted_meetings[0][1], new_room_number))
        counts[new_room_number] += 1

        for i in range(1, len(sorted_meetings)):
            start, end = sorted_meetings[i]
            smallest_end, room_number = timers_heap[0]

            if smallest_end <= start:
                while len(timers_heap) > 0 and timers_heap[0][0] <= start:
                    _, room_number = heapq.heappop(timers_heap)
                    heapq.heappush(unused_rooms_heap, room_number)

            if len(unused_rooms_heap) > 0:
                new_room_number = heapq.heappop(unused_rooms_heap)
                heapq.heappush(timers_heap, (end, new_room_number))
                counts[new_room_number] += 1
            else:
                heapq.heappop(timers_heap)
                heapq.heappush(timers_heap, (smallest_end + end - start, room_number))
                counts[room_number] += 1

        result = None
        max_count = -math.inf
        for room_number, count in counts.items():
            if count > max_count:
                result = room_number
                max_count = count

        return result


"""
Sorted?
"""

"""
n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
                                       ^

Possible Rooms: Min Heap []

Timer: Min Heap [(10, 1), (11, 0)]

counts = {
    0: 2
    1: 2
}
"""

"""
In both "253. Meeting Rooms II" and this problem, the core idea is using a Min Heap to quickly retrieve the earliest end time.

However, there is a fundamental principle to remember when solving heap-based problems. Only currently available items should exist in the heap, and you must stick to that rule strictly.

Specifically, in this problem, you need to use two heaps to ensure that only available resources are stored. You should maintain both a `timers_heap` and an `unused_rooms_heap` to manage
the state effectively.
"""
