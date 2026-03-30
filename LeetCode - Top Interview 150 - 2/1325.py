class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def dfs_remove_node(node, target):
            if not node:
                return

            node.left = dfs_remove_node(node.left, target)
            node.right = dfs_remove_node(node.right, target)

            if not node.left and not node.right and node.val == target:
                return

            return node

        return dfs_remove_node(root, target)
