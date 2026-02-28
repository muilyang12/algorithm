import heapq


class MedianFinder:
    def __init__(self):
        self.left_half = []
        self.right_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.right_half, num)

        if (len(self.left_half) + len(self.right_half)) % 2 == 0:
            heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

        if (
            len(self.left_half) + len(self.right_half) >= 2
            and -self.left_half[0] > self.right_half[0]
        ):
            max_from_left = -heapq.heappop(self.left_half)
            min_from_right = heapq.heappop(self.right_half)

            heapq.heappush(self.left_half, -min_from_right)
            heapq.heappush(self.right_half, max_from_left)

    def findMedian(self) -> float:
        if (len(self.left_half) + len(self.right_half)) % 2 == 0:
            return (-self.left_half[0] + self.right_half[0]) / 2
        else:
            return self.right_half[0]


"""
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

self.left_half = [1] => Max Heap
self.right_half = [2, 3] => Min Heap

["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]

self.left_half = [3, 4]
self.right_half = [-2, -1]
"""
