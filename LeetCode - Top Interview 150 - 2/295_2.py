class MedianFinder:
    def __init__(self):
        self.left_half = []
        self.right_half = []

    def addNum(self, num: int) -> None:
        if not self.left_half and not self.right_half:
            heapq.heappush(self.left_half, -num)
        elif len(self.left_half) == len(self.right_half) and num >= -self.left_half[0]:
            heapq.heappush(self.right_half, num)
            num_to_move = heapq.heappop(self.right_half)
            heapq.heappush(self.left_half, -num_to_move)
        elif len(self.left_half) == len(self.right_half) and num < -self.left_half[0]:
            heapq.heappush(self.left_half, -num)
        elif len(self.left_half) > len(self.right_half) and num >= -self.left_half[0]:
            heapq.heappush(self.right_half, num)
        elif len(self.left_half) > len(self.right_half) and num < -self.left_half[0]:
            num_to_move = -heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, num_to_move)
            heapq.heappush(self.left_half, -num)

    def findMedian(self) -> float:
        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2
        else:
            return -self.left_half[0]


"""
The core logic here is deciding whether the incoming value should go to the left_half or the right_half. While the approach of inserting into the left and then adjusting is good, I think a case-by-case
classification could also work.

1. The case where `len(left) == len(right)` and the incoming value belongs in the `left_half`.
2. The case where `len(left) == len(right)` and the incoming value belongs in the `right_half`.
3. The case where `len(left) + 1 == len(right)` and the incoming value belongs in the `left_half`.
4. The case where `len(left) + 1 == len(right)` and the incoming value belongs in the `right_half`.

Having four `if` statements might seem a bit much, but this approach allows for very precise filtering of each scenario.

The absolute first priority in this problem is realizing that you need to use a Heap. The second priority is maintaining the balance between the left and right sides, whether through adjustments or a
case-by-case classification.
"""


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
