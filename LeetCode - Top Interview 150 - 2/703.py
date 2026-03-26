class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.left_array = []
        self.right_array = []

        for num in nums:
            heapq.heappush(self.right_array, num)

            if len(self.right_array) > k:
                heapq.heappush(self.left_array, -heapq.heappop(self.right_array))

    def add(self, val: int) -> int:
        heapq.heappush(self.right_array, val)

        if len(self.right_array) > self.k:
            heapq.heappush(self.left_array, -heapq.heappop(self.right_array))

        return self.right_array[0]
