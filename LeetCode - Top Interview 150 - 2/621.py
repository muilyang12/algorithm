"""
To determine when to re-insert a specific task into the heap, I initially used a hash structure like `{task: time_left}` and subtracted 1 from the time_left in every cycle. However, this approach has a time
complexity of O(n * k) (where k is the number of distinct tasks) because it requires iterating through the cooldown hash during each step.

The method suggested by Gemini is much more efficient. Since we know the minimum duration a task must wait before its next execution, we can predict exactly when it should return to the heap. By using a
`timer` variable and a Queue to store `(time_to_return, task)` pairs, we can simply use queue.popleft() when the timer reaches that specific point. This reduces the complexity to O(n) for the cooling logic.
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = {}
        for task in tasks:
            if task not in task_counts:
                task_counts[task] = 0

            task_counts[task] += 1

        heap = []
        for key, val in task_counts.items():
            heapq.heappush(heap, (-val, key))

        cooldown_left = {}
        result = 0

        while heap or cooldown_left:
            ready_to_back = []

            for task in cooldown_left:
                if cooldown_left[task] == 0:
                    ready_to_back.append(task)
                    
                cooldown_left[task] -= 1

            for task in ready_to_back:
                del cooldown_left[task]
                heapq.heappush(heap, (-task_counts[task], task))

            if heap:
                count_left, task = heapq.heappop(heap)
                
                task_counts[task] -= 1
                
                if task_counts[task] > 0:
                    cooldown_left[task] = n

            result += 1

        return result


"""
The problem itself didn't seem too difficult at first. It's categorized under 'Heap,' but I thought I could solve it using just a Hash.

However, after trying it out, I realized that a Hash map alone isn't enough. If you pick tasks in a random order, you can't achieve the minimum time because idle slots are wasted at the end. For example,
given {A:1, B:2} and n=2, a random order might result in A -> B -> I -> I -> B, whereas the optimal sequence is B -> A -> I -> B. To avoid this, you must execute the task with the highest frequency first.

So, I tried using a combination of Sorting and Hash, but that didn't work either. Take {A:4, B:1, C:1, D:1, E:1} with n=1 as an example. Comparing A -> B -> C -> D -> E -> A -> I -> A -> I -> A versus
A -> B -> A -> C -> A -> D -> A -> E, the latter is clearly more efficient. The sorting approach fails because it doesn't account for the need to interleave low-frequency tasks between high-frequency ones
to minimize idle time.

Now I see why this is categorized under 'Heap.' Other methods all seem to have flaws. This problem is genuinely tough.

The core idea for solving this problem is to always execute the task with the maximum remaining count among the currently available tasks. To constantly pick the maximum, using a Heap is required. Furthermore,
you need to introduce an additional data structure to manage when a task can be re-inserted into the heap.
"""

"""
tasks = ["A","A","A","B","B"], n = 2

duration_each_cycle = 3
max_count = 3
rest = 1

duration_each_cycle * (max_count - 1) + rest = 7

A B I A B I A

=====

tasks = ["A","C","A","B","D","B"], n = 1

duration_each_cycle = 4
max_count = 3
rest = 1
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = {}
        for task in tasks:
            if task not in task_counts:
                task_counts[task] = 0

            task_counts[task] += 1

        count_task_tuples = []
        for key, value in task_counts.items():
            count_task_tuples.append((value, key))
        count_task_tuples = sorted(count_task_tuples, key=lambda x: x[0])

        duration_each_cycle = max(len(count_task_tuples), n + 1)
        max_count = count_task_tuples[-1][0]

        rest = 0
        for i in range(len(count_task_tuples)):
            if count_task_tuples[len(count_task_tuples) - 1 - i][0] == max_count:
                continue

            rest = i + 1

        return duration_each_cycle * (max_count - 1) + rest


"""
Initially, I assumed that the duration_each_cycle would be a fixed value, but it turned out not to be the case.
"""
