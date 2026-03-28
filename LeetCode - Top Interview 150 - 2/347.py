# Time Complexity: O(n + (m - k) log k) = O(n log k), Space Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Create a dictionary named `num_counts` and populate it with the frequency of each number.
        2. Iterate through the dictionary using a loop such as `for num, count in num_counts.items()`.
        3. Insert each pair as `(count, num)` into a Min-Heap.
        4. Perform `heappop(heap)` whenever the `len(heap)` exceeds k to ensure that only the top k elements remain.
        """


import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if not num in counts:
                counts[num] = 0

            counts[num] += 1

        heap = []
        for key, val in counts.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for _, key in heap:
            result.append(key)

        return result


"""
nums = [1,1,1,2,2,3], k = 2

{
    1: 3
    2: 2
    3: 1
}

for key, val incount.items()

(val, key)

heap[(3, 1), (2, 2), (1, 3)]

Top K

len(heap) > k

heappop()
"""

"""
Use a min-heap for Top K Largest and a max-heap for Top K Smallest.
"""

"""
When I want to find the $K$-th largest element or the top K elements, I should use a Min Heap and call heappop whenever the heap size exceeds K.
"""