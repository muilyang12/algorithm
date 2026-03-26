class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        sorted_tasks = sorted(sorted_tasks)

        timer = 0
        count_done = 0
        current = 0

        heap = []

        result = []

        while count_done < len(sorted_tasks):
            while current < len(sorted_tasks) and sorted_tasks[current][0] <= timer:
                heapq.heappush(
                    heap, (sorted_tasks[current][1], sorted_tasks[current][2])
                )
                current += 1

            if len(heap) > 0:
                processing_time, index = heapq.heappop(heap)

                result.append(index)
                timer += processing_time

                count_done += 1

            else:
                timer = sorted_tasks[current][0]

        return result


"""
[[1,2],[2,4],[3,2],[4,1]] [1, 4]
timer 5
current 4
count 3

=====

[[7,10],[7,12],[7,5],[7,4],[7,2]] [(2, 4), (4, 3), ...]
timer 7
current 5
count 0
"""

"""
For this problem as well, instead of putting everything from the tasks list into the heap at once, you should push them into the heap only when they become executable based on the time. In that regard,
the idea is quite similar to the "621. Task Scheduler" problem.

Also, when using a timer, incrementing it strictly by += 1 is not the best approach. Since the next task can only start once the timer reaches a certain point, it is much better to skip directly to that
time. This is an idea that can also be applied to "621. Task Scheduler."
"""
