# Time Complexity: O(n log n)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True

        arr = sorted(arr)

        diff = abs(arr[1] - arr[0])

        for i in range(2, len(arr)):
            if abs(arr[i] - arr[i - 1]) != diff:
                return False

        return True
