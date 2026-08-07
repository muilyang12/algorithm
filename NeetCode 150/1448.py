class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, max_so_far):
            nonlocal result

            if not node:
                return

            if node.val >= max_so_far:
                result += 1

            dfs(node.left, max(max_so_far, node.val))
            dfs(node.right, max(max_so_far, node.val))

        dfs(root, root.val)

        return result
