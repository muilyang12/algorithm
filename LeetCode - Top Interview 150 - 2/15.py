# O(n^2) // O(2n)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)

        result = []
        set_for_check = set()

        for index in range(len(nums) - 2):
            left = index + 1
            right = len(nums) - 1

            while left < right:
                if sorted_nums[left] + sorted_nums[right] == -sorted_nums[index]:
                    if (
                        sorted_nums[index],
                        sorted_nums[left],
                        sorted_nums[right],
                    ) in set_for_check:
                        left += 1
                        right += 1
                        continue

                    set_for_check.add(
                        (sorted_nums[index], sorted_nums[left], sorted_nums[right])
                    )
                    result.append(
                        [sorted_nums[index], sorted_nums[left], sorted_nums[right]]
                    )
                    left += 1
                    right += 1
                elif sorted_nums[left] + sorted_nums[right] > -sorted_nums[index]:
                    right -= 1
                else:
                    left += 1

        return result


"""
for
for
for
O(n^3)

O(n^2)

[-1,0,1,2,-1,-4]

[-4, -1, -1, 0, 1, 2]
  ^
             ^     ^
"""
