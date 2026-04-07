"""
This reminds me of a recent NeetCode video where he reflected on an interview he took in the past. In that video, he expressed regret because he tried to avoid using global variables
without even checking with the interviewer, even though doing so would have made the problem much easier to solve. This problem might be the very one he was talking about.
"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -math.inf

        def dfs_one_way_path_sum(node):
            if not node:
                return 0

            left_path_sum = dfs_one_way_path_sum(node.left)
            right_path_sum = dfs_one_way_path_sum(node.right)

            self.max_sum = max(
                self.max_sum, node.val + max(0, left_path_sum) + max(0, right_path_sum)
            )

            return node.val + max(0, left_path_sum, right_path_sum)

        dfs_one_way_path_sum(root)

        return self.max_sum


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs_get_max_sum(node):
            if not node:
                return (0, -math.inf)

            left_one_way_sum, left_max_path_sum = dfs_get_max_sum(node.left)
            right_one_way_sum, right_max_path_sum = dfs_get_max_sum(node.right)

            current_one_way_sum = max(0, left_one_way_sum, right_one_way_sum) + node.val
            current_path_sum = node.val
            current_path_sum += left_one_way_sum if left_one_way_sum > 0 else 0
            current_path_sum += right_one_way_sum if right_one_way_sum > 0 else 0

            return (
                current_one_way_sum,
                max(current_path_sum, left_max_path_sum, right_max_path_sum),
            )

        _, max_path_sum = dfs_get_max_sum(root)

        return max_path_sum


"""
The approach feels quite familiar, but the actual implementation is considerably difficult. I think I need to practice implementing this one more time.

This problem is essentially identical to "543. Diameter of Binary Tree". I'm glad I practiced the approach of returning both the height and the maximum diameter, rather than just stopping
at the solution using `self.result`.

The core idea is to have the DFS function return a pair consisting of the `one_way_sum` and the `max_path_sum`. Just as `height` was a building block for calculating the diameter in the
previous problem, the `one_way_sum` serves as the building block for calculating the path sum. By passing both the building block and the current maximum path sum, we can continuously update
the max value while returning the results.

However, since height and maximum diameter are always positive, conditions like taking only positive values were unnecessary. In this problem, we must include a condition like max(0, ____)
to ensure we only consider positive contributions.

The most confusing part was whether to include the current node's value when calculating the current_one_way_sum and current_path_sum. Specifically, I struggled with whether to pass the
negative value or zero if the node itself is negative and the cumulative value up to that point is also negative. I decided to unconditionally include the current node's value. As long as
the definition is clear and the implementation follows that definition, I believe either approach can work.
"""
