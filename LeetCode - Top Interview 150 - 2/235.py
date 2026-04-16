"""
In a BST, if the current node's value is between `p` and `q`, we can conclude that the current node is the LCA. This allows us to implement the logic as follows.

Don't be too conservative about using instance variables like `self.result`. You should stay open to using them after confirming with the team, as they can significantly
simplify the logic.
"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.result = None

        def dfs_find_lca(node):
            if not node:
                return

            if self.result:
                return

            if p.val <= node.val <= q.val or p.val >= node.val >= q.val:
                self.result = node
                return

            dfs_find_lca(node.left)
            dfs_find_lca(node.right)

        dfs_find_lca(root)

        return self.result


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs_find_lca(node):
            if not node:
                return

            if p.val <= node.val <= q.val or p.val >= node.val >= q.val:
                return node

            return dfs_find_lca(node.left) or dfs_find_lca(node.right)

        return dfs_find_lca(root)


"""
This problem is a variation of "236. Lowest Common Ancestor of a Binary Tree," but I overlooked the specific constraints and solved it the same way. In a BST, unlike
a general BT, there is a strict rule regarding value ordering. I should have leveraged this property from the start.
"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.result = None

        def dfs_has_target_nodes(node):
            if not node:
                return (False, False)
            if self.result:
                return (False, False)

            left_search = dfs_has_target_nodes(node.left)
            right_search = dfs_has_target_nodes(node.right)

            current_result = (
                node == p or left_search[0] or right_search[0],
                node == q or left_search[1] or right_search[1],
            )

            if current_result[0] and current_result[1]:
                self.result = node
                return (False, False)
            else:
                return current_result

        dfs_has_target_nodes(root)

        return self.result
