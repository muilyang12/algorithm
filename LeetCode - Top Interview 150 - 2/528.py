"""
This is a very simple yet great problem that utilizes Prefix Sum and Binary Search.

You did well in calculating the weights using the Prefix Sum method. However the pickIndex function could be improved. Since you know that self.weights contains values between 0 and 1 and they are already sorted
you can use Binary Search to find a range or a value. This would reduce the time complexity to O(log n).

By the way,remember how to use the `random` module.
random.random() -> floating point number between 0.0 and less than 1.0
random.randrange(1, 10) -> integer between 1 and less than 10
random.randint(1, 10) -> integer between 1 and 10 inclusive
"""


# Time Complexity: O(log n) (n: length of w)
class Solution:
    def __init__(self, w: List[int]):
        self.weights = [0 for _ in w]
        self.weights[0] = w[0]
        for i in range(1, len(self.weights)):
            self.weights[i] = self.weights[i - 1] + w[i]

        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] / self.weights[-1]

    def pickIndex(self) -> int:
        current = random.random()

        left = 0
        right = len(self.weights) - 1

        while left <= right:
            mid = (left + right) // 2

            if current < self.weights[mid]:
                right = mid - 1
            elif current > self.weights[mid]:
                left = mid + 1
            else:
                return mid

        return left


# Time Complexity: O(n) (n: length of w)
class Solution:
    def __init__(self, w: List[int]):
        self.weights = [0 for _ in w]
        self.weights[0] = w[0]
        for i in range(1, len(self.weights)):
            self.weights[i] = self.weights[i - 1] + w[i]

        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] / self.weights[-1]

    def pickIndex(self) -> int:
        current = random.random()

        for i in range(len(self.weights)):
            weight = self.weights[i]

            if current < weight:
                return i
