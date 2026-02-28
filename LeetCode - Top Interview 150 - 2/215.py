import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)


"""
nums = [3,2,1,5,6,4], k = 2

[3, 5, 6]

"""
