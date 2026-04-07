"""
heap = [] -> Min Heap
num_people = 0

trips = [[2,1,5],[3,3,7]]
                  ^

heap = [(5, 2)]
num_people = 2

trips = [[2,1,5],[3,5,7]]
                          ^
heap = [(7,3)]
num_people = 3

=====

Time Complexity: O(n log n), Space Complexity: O(n)

=====

Edge Cases
- [0, 3, 5]
- [3, 5, 5]
- trips = []
- trips = [[100, 1, 5]]
"""


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key=lambda x: x[1])
        current = 0

        heap = []

        people_in_car = 0
        position = 0

        while current < len(sorted_trips) or heap:
            while heap and position == heap[0][0]:
                _, num_passenger = heapq.heappop(heap)

                people_in_car -= num_passenger

            while current < len(sorted_trips) and position == sorted_trips[current][1]:
                num_passenger, from_pos, to_pos = sorted_trips[current]
                heapq.heappush(heap, (to_pos, num_passenger))

                current += 1
                people_in_car += num_passenger

                if people_in_car > capacity:
                    return False

            if heap and current < len(sorted_trips):
                position = min(heap[0][0], sorted_trips[current][1])
            elif heap:
                position = heap[0][0]
            elif current < len(sorted_trips):
                position = sorted_trips[current][1]
            else:
                position += 1

        return True


"""
The key in heap-based problems involving a timer is how well you can jump the `timer` forward. For this problem, the current location of the vehicle, `position`, acts as the `timer`. Therefore,
it is crucial to jump the current `position` by considering both the next pickup location in the sorted_trips and the earliest drop-off location currently in the heap.
"""


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key=lambda x: x[1])
        current = 0

        heap = []

        people_in_car = 0
        position = 0

        while current < len(sorted_trips) or heap:
            while heap and position == heap[0][0]:
                _, num_passenger = heapq.heappop(heap)

                people_in_car -= num_passenger

            while current < len(sorted_trips) and position == sorted_trips[current][1]:
                num_passenger, from_pos, to_pos = sorted_trips[current]
                heapq.heappush(heap, (to_pos, num_passenger))

                current += 1
                people_in_car += num_passenger

                if people_in_car > capacity:
                    return False

            if not heap and current < len(sorted_trips):
                position = sorted_trips[current][1]
            else:
                position += 1

        return True


"""
trips = [[2,1,5],[3,3,7]]
"""
