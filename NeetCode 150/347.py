class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if not num in counts:
                counts[num] = 0

            counts[num] += 1

        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (-count, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
