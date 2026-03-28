class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs_inorder(node, values):
            if not node:
                return

            if len(values) >= k:
                return

            dfs_inorder(node.left, values)
            values.append(node.val)
            dfs_inorder(node.right, values)

        values = []
        dfs_inorder(root, values)

        return values[k - 1]


# Time Complexity: O(k), O(k + h), O(n), Space Complexity: O(h), O(k), O(k + h)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs_inorder(node, values):
            if not node:
                return None

            if len(values) < k:
                dfs_inorder(node.left, values)
            if len(values) < k:
                values.append(node.val)
            if len(values) < k:
                dfs_inorder(node.right, values)

        values = []
        dfs_inorder(root, values)

        return values[-1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs_inorder(node, values):
            if not node:
                return None

            dfs_inorder(node.left, values)
            values.append(node.val)
            dfs_inorder(node.right, values)

        values = []
        dfs_inorder(root, values)

        return values[k - 1]
