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