class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0
        fruit_counts = {}

        left = 0
        right = 0

        while right < len(fruits):
            if fruits[right] not in fruit_counts:
                fruit_counts[fruits[right]] = 0

            fruit_counts[fruits[right]] += 1

            while len(fruit_counts) > 2:
                fruit_counts[fruits[left]] -= 1

                if fruit_counts[fruits[left]] == 0:
                    del fruit_counts[fruits[left]]

                left += 1

            result = max(result, right - left + 1)

            right += 1

        return result


"""
fruit_types = {2: 3, 3: 0}
result = 4

fruits = [1,2,3,2,2]
            !
                    @

left
right

Sliding Window
"""
