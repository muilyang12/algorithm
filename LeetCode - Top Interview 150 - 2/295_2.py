class MedianFinder:
    def __init__(self):
        self.left_half = []
        self.right_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_half, -num)

        if (
            self.left_half
            and self.right_half
            and -self.left_half[0] > self.right_half[0]
        ):
            num_from_left = heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, -num_from_left)
            num_from_right = heapq.heappop(self.right_half)
            heapq.heappush(self.left_half, -num_from_right)

        if len(self.left_half) > len(self.right_half):
            num_to_move = heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, -num_to_move)

    def findMedian(self) -> float:
        if (len(self.left_half) + len(self.right_half)) % 2 == 0:
            return (-self.left_half[0] + self.right_half[0]) / 2
        else:
            return self.right_half[0]


"""
I felt that my previous solution was a bit too complex, so this time I wanted to keep the algorithm simpler. I went with a straightforward approach by always inserting the new value into the `left_half`
and moving the maximum value to the right if it overflows. That is the algorithm shown below.

However, this algorithm has a limitation. The problem is that the comparison and adjustment between the left and right sides only happen when the `left_half` overflows. Suppose a larger value comes in
later. If the `left_half` doesn't overflow, no adjustment will be triggered, and that larger value will remain on the left side. 

So, I need to improve the logic. Even if I insert into the left side first, I should make it a rule to always check for a swap between the two sides, rather than only checking when it overflows. Then,
if the `left_half` happens to overflow at that point, I would perform one more move.
"""


class MedianFinder:
    def __init__(self):
        self.left_half = []
        self.right_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_half, -num)

        if len(self.left_half) > len(self.right_half):
            num_to_move = -heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, num_to_move)

    def findMedian(self) -> float:
        if (len(self.left_half) + len(self.right_half)) % 2 == 0:
            return (-self.left_half[0] + self.right_half[0]) / 2
        else:
            return self.right_half[0]
