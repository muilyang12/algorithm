class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs_bst_delete(node, key):
            if not node:
                return None

            if node.val > key:
                node.left = dfs_bst_delete(node.left, key)
                return node
            elif node.val < key:
                node.right = dfs_bst_delete(node.right, key)
                return node
            else:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    last = node.left
                    while last.right:
                        last = last.right

                    node.val = last.val
                    node.left = dfs_bst_delete(node.left, last.val)
                    return node

        return dfs_bst_delete(root, key)


"""
This problem is truly difficult. I think I need to practice not just the core idea, but the logic implementation as well.

First of all, when creating the `def dfs_find(node):` function, I must leverage the characteristics of a BST. I just used DFS to perform a full traversal without much thought. That's not right. If the
key is smaller than the current node's value, I should go left, and if it's larger, I should go right. In a BST, the time complexity for finding a value is O(h), O(log n), or O(n). That's exactly the
reason why.

I think effectively using the return value in a `dfs` function is truly important in tree problems. Remember how we used return count in the "Good Nodes" problem? In this case, it's crucial to have the
function return a node or None. That way, when you do `node.left = dfs(node.left)`, the parent can properly point to its updated child after the operation.

Lastly, you must know exactly how to fill the gap when deleting a node in a BST. You should replace it with either the maximum value from the left subtree or the minimum value from the right subtree.
If you simply promote the left child to the deleted node's position, the new parent could end up being smaller than one of the nodes in its own left subtree. This would violate the fundamental BST
property where every node in the left subtree must be smaller than the parent.
"""

"""
In tree problems like this, we often use h to express complexity. While h is log n if the tree is balanced, it can also be n in the worst case. I think it's better if I mention this point
first.
"""
