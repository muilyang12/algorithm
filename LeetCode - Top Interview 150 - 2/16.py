class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)

        current_diff = math.inf
        result = target

        for i in range(len(sorted_nums) - 2):
            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                current_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if current_sum == target:
                    return target

                if abs(target - current_sum) < current_diff:
                    current_diff = abs(target - current_sum)
                    result = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
