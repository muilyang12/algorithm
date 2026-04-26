"""
For this problem, we first need to identify which two nodes in the given BST have swapped values. By performing an inorder traversal and listing the values, we can
easily spot the two nodes where the ascending order is broken. Once those two nodes are identified, we simply swap their values to restore the BST.

What I found slightly regrettable in my initial approach was trying to swap everything, including the `left` and `right` pointers. That is unnecessary because the
structural connections of the nodes are already correct. Since the positions are fine, the problem can be easily implemented by just swapping the `val` of the two nodes.
"""


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.values = []

        def dfs_inorder(node):
            if not node:
                return

            dfs_inorder(node.left)
            if node:
                self.values.append((node.val, node))
            dfs_inorder(node.right)

        dfs_inorder(root)

        left = -1
        right = -1

        for i in range(len(self.values) - 1):
            if self.values[i][0] > self.values[i + 1][0]:
                if left < 0:
                    left = i
                if left >= 0:
                    right = i + 1

        temp_val = self.values[left][1].val
        self.values[left][1].val = self.values[right][1].val
        self.values[right][1].val = temp_val
