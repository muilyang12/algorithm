# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while left < right and right - left + 1 > k:
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1

        return arr[left : right + 1]


# Time Complexity: O(n log n + k log k) = O(n log n), Space Complexity: O(k)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff_arr = [(abs(arr[i] - x), i, arr[i]) for i in range(len(arr))]
        sorted_diff_arr = sorted(diff_arr)

        result = []
        for i in range(k):
            _, _, num = sorted_diff_arr[i]
            result.append(num)

        result = sorted(result)

        return result


"""
Length > k?
Same difference?
"""

"""
For this problem, three different approaches come to mind.
1. Using a Heap, similar to "215. Kth Largest Element in an Array."
2. Creating a `diff_arr` and then sorting it. This is the least efficient approach since sorting takes O(n log n).
3. Using the Two Pointer approach, which is the most efficient.
"""

"""
You should always raise questions in these situations. What if there are two items with the same interval and you have to choose only one? You must be able to think in this manner. It is essential to read
the problem accurately before diving in.
"""


# Time Complexity: O(n log k + k log k) = O(n log k), Space Complexity: O(k)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            heapq.heappush(heap, (-abs(x - num), -num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = [-num for _, num in heap]
        result = sorted(result)

        return result
