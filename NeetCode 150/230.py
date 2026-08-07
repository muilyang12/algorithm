class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nth = k
        result = None

        def dfs(node):
            nonlocal nth, result

            if not node:
                return

            dfs(node.left)

            nth -= 1
            if nth == 0:
                result = node.val

            dfs(node.right)

        dfs(root)

        return result
