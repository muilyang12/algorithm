class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_check_bst_validity(node, min_value, max_value):
            if not node:
                return True

            if node.val <= min_value or node.val >= max_value:
                return False

            return dfs_check_bst_validity(
                node.left, min_value, node.val
            ) and dfs_check_bst_validity(node.right, node.val, max_value)

        return dfs_check_bst_validity(root, -math.inf, math.inf)


"""
While looking at the definition of a BST to solve this problem, I was unsure whether to include the equal sign in the inequality `if node.val <= min_val or node.val >= max_val`. After discussing it
with Gemini, I learned that the definition of a BST can vary depending on the context. However, since the problem explicitly states "strictly less than", it is correct to include the equal sign in
the check to invalidate duplicate values.
"""


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
