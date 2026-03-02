# O(n^3) // O(2n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)

        result = []
        check_for_dup = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    if sorted_nums[left] + sorted_nums[right] == target - sorted_nums[i] - sorted_nums[j]:
                        if (sorted_nums[i], sorted_nums[j], sorted_nums[left], sorted_nums[right]) in check_for_dup:
                            left += 1
                            right -= 1
                            continue

                        result.append([sorted_nums[i], sorted_nums[j], sorted_nums[left], sorted_nums[right]])
                        check_for_dup.add((sorted_nums[i], sorted_nums[j], sorted_nums[left], sorted_nums[right]))
                        left += 1
                        right -= 1
                    elif sorted_nums[left] + sorted_nums[right] < target - sorted_nums[i] - sorted_nums[j]:
                        left += 1
                    else:
                        right -= 1
        
        return result



"""
for for for for
O(n^4)

nums = [1,0,-1,0,-2,2]

[-2,-1,0,0,1,2]
 ^   ^     ^ ^
 ^     ^ ^   ^
"""