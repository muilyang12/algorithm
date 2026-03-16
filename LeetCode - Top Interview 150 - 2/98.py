class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_validate(node, min_val, max_val):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return dfs_validate(node.left, min_val, node.val) and dfs_validate(
                node.right, node.val, max_val
            )

        return dfs_validate(root, -math.inf, math.inf)
