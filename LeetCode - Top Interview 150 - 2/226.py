class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs_invert_tree(node):
            if not node:
                return

            temp = node.left
            node.left = dfs_invert_tree(node.right)
            node.right = dfs_invert_tree(temp)

            return node

        return dfs_invert_tree(root)


"""
I was able to quickly figure out the general direction of using recursion to invert the tree, such as `node.left = dfs_invert_tree(node.right)`. However, I realized that if I call the logic that way,
the reference to the original node.left disappears, so I must store it in a temporary variable beforehand. It is just like using a `temp` variable when swapping two values.

Although I didn't perform a dry run this time, I must always do a dry run when solving this type of problem in a real-world scenario to catch these kinds of errors.
"""
