import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            heapq.heappush(heap, (math.sqrt(point[0] ** 2 + point[1] ** 2), point))

        result = []
        for _ in range(k):
            _, point = heapq.heappop(heap)
            result.append(point)

        return result
