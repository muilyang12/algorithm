class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_get_height(node):
            if not node:
                return 0

            left_height = dfs_get_height(node.left)
            if left_height == -1:
                return -1
            right_height = dfs_get_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return dfs_get_height(root) != -1


"""
Designing the function correctly is extremely important for this problem. The fundamental role of the `dfs` function should be to return the height of the current node, but
you must also incorporate a mechanism to return -1 if the heights of the two child nodes are not balanced. If you can clearly visualize this approach of using a specific
value like -1 to signal a balance failure, the problem becomes much less difficult to solve.
"""
