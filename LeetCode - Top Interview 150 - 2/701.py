class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs_insert(node, val):
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = self.insertIntoBST(root.left, val)
            elif val > node.val:
                node.right = self.insertIntoBST(root.right, val)

            return node

        return dfs_insert(root, val)


"""
Since I solved "450. Delete Node in a BST" with Gemini right before this one, I think I was able to solve it relatively easily. The core idea here is exactly the same, where I write the `dfs` function
using the `node.left = dfs(node.left)` pattern. In other words, the key to this problem is ensuring that the dfs function returns either a node or None.
"""
