class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        left = 1
        right = max_pile

        while left <= right:
            mid = (left + right) // 2

            days_taken = self.get_days_taken(piles, mid)
            if days_taken > h:
                left = mid + 1
            elif days_taken <= h:
                right = mid - 1

        return left

    def get_days_taken(self, piles, amount_for_a_day):
        days = 0
        for pile in piles:
            days += ceil(pile / amount_for_a_day)

        return days
