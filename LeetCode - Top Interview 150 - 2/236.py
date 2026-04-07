class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs_check_pq(node):
            if not node:
                return None

            if node == p or node == q:
                return node

            left = dfs_check_pq(node.left)
            right = dfs_check_pq(node.right)

            if left and right:
                return node

            if left:
                return left

            if right:
                return right

            return None

        return dfs_check_pq(root)
