class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = {}
        for task in tasks:
            task_counts[task] = task_counts.get(task, 0) + 1

        heap = []
        for task, count in task_counts.items():
            heapq.heappush(heap, (-count, task))

        cooldown = deque()
        timer = 0

        while heap or cooldown:
            if not heap and cooldown[0][2] > timer:
                timer = cooldown[0][2]
                continue
            elif cooldown and cooldown[0][2] == timer:
                task, count, _ = cooldown.popleft()

                heapq.heappush(heap, (-count, task))

            count, task = heapq.heappop(heap)
            count = -count
            count -= 1

            if count > 0:
                cooldown.append((task, count, timer + n + 1))

            timer += 1

        return timer
