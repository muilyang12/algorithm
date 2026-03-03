class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] < nums[right]:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid] and target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return left if nums[left] == target else -1


"""
5,6,7,8,0,1,2,3,4 // 3
^     p ^       ^
          ^ m   ^
              ^ ^
              m

- mid < right
left pivot mid right

- mid > right
left mid pivot right

[1,3]
 ^ ^
 m

Edge cases
[1,2,3,4,5] // 3 -> When there is no rotation.
[1,2,4,5,6] // 3 -> When there is no target value.
[5,6,7,8,0,1,2,3,4] // 4 -> In binary search, boundary equal is hard to decide
[5,6,7,8,0,1,2,3,4] // 5
[5,6,7,8,0,1,2,3,4] // 8
"""


"""
The key idea here is to split cases based on the pivot's location to determine which segment to search.
"""