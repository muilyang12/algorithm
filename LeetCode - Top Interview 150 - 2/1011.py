class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def count_days(capacity):
            days = 0
            current_sum = 0
            for weight in weights:
                current_sum += weight

                if current_sum > capacity:
                    days += 1
                    current_sum = weight
            
            if current_sum > 0:
                days += 1

            return days

        left = max(weights)
        right = sum(weights)

        result = math.inf

        while left <= right:
            mid = (left + right) // 2

            if count_days(mid) <= days:
                result = min(result, mid)

                right = mid - 1
            else:
                left = mid + 1

        return result


"""
Gemini mentioned that this problem is identical to 410. Split Array Largest Sum. That is why I am trying to solve them back-to-back, and it turns out they really are exactly the same.

The fundamental idea of Binary Search is to find a value that satisfies a specific condition within a certain range. However, it is honestly very difficult to recognize this pattern
when first looking at the problem.
"""
