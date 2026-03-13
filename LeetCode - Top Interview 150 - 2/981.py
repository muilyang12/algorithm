class TimeMap:
    def __init__(self):
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = []

        self.hash[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ""

        left = 0
        right = len(self.hash[key]) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.hash[key][mid][0] <= timestamp:
                left = mid + 1
            elif self.hash[key][mid][0] > timestamp:
                right = mid - 1

        return self.hash[key][right][1] if right >= 0 else ""


"""
Assume timestamp positive
Not existing value also "", right?
If same timestamp comes in?
Timestamp increasing?
"""

"""
I came into this problem knowing it should be solved with Binary Search. My first thought is to use a dictionary where each value is a list of (timestamp, value) tuples, sorted by timestamp.

The challenge is how to maintain the sorted order of the list by timestamp.

The simplest way is to call `append()` and `sorted()` every time. This would maintain the order with O(N log N) time complexity.

Another way is to use binary search to find the correct index and then insert the element. This allows finding the index in O(log N), and since the insertion itself takes O(N), we can maintain
the sorted state in O(N) time.

On second thought, I considered sorting because I assumed timestamps would arrive in a random order. I should not have made such an assumption.

There were no questions about the timestamp in my question list. It seems I proceeded with my own assumptions without even thinking to ask for clarification. I must not assume anything. I need to
ask about every detail to make everything clear before proceeding.
"""
