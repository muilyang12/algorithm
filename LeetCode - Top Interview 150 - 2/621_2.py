class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = {}
        for task in tasks:
            if task not in task_counts:
                task_counts[task] = 0

            task_counts[task] += 1

        heap = []
        for task, count in task_counts.items():
            heapq.heappush(heap, (-count, task))

        cooldown_queue = deque()

        timer = 0

        while heap or cooldown_queue:
            while len(cooldown_queue) > 0 and cooldown_queue[0][0] <= timer:
                _, task, count = cooldown_queue.popleft()
                heapq.heappush(heap, (-count, task))

            if heap:
                count, task = heapq.heappop(heap)
                count = -count

                if count - 1 > 0:
                    cooldown_queue.append((timer + n + 1, task, count - 1))

                timer += 1
            else:
                timer = cooldown_queue[0][0]

        return timer


"""
I think I need to keep practicing this problem even after today. It is truly difficult.

Multiple ideas are required to solve it, such as the idea of pushing only the processable tasks into the heap, and using a queue to manage the cooldown period. Another key is the concept of using a timer.
When the heap is empty, instead of incrementing the timer by one, a better approach is to jump the timer directly to the point when the first task in the cooldown queue can be released.
"""
