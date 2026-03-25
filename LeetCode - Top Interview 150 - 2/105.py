# Time Complexity: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_node_index_map = { inorder[i]: i for i in range(len(inorder))}

        def dfs_build(pre_start, pre_end, in_start, in_end):
            in_root_index = in_node_index_map[preorder[pre_start]]
            
            node = TreeNode(preorder[pre_start])

            node.left = dfs_build(pre_start + 1)
            node.right = dfs_build()

            return node

        return dfs_build(0, len(preorder) - 1, 0, len(inorder) - 1)


"""
I'm not going to finish it right now. I just want to write up to that point.

At first, I wrote it in a way that recursively calls the buildTree function itself using slicing. The "Solution" below follows that approach. With that method, the time complexity is O(n * (n + n)),
which results in  O(n^2). We can optimize this in two aspects. By removing each of the n + n parts, we can eventually achieve O(n).

1. I'm going to use a method that passes indices, like `def build_tree_with_index(pre_start, pre_end, in_start, in_end):`. If I do it this way, I don't need to perform slicing, so I can eliminate
one of the n terms.
2. For the inorder traversal, I'm planning to create a hash like { value: index }. This way, I can eliminate the use of a for-loop to find the root's index in the inorder list. This removes the
remaining n term.

In short, the time complexity will become O(n).

However, thinking about it again, the second optimization requires the values to be unique. Do you remember, perhaps in the 133. Clone Graph problem, where the values weren't unique, so we had to use
the node itself as the key? It's similar to that.
"""


# Time Complexity: O(n^2)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])

        root_index = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root_index = i
                break

        left_count = root_index

        root.left = self.buildTree(preorder[1 : 1 + left_count], inorder[:root_index])
        root.right = self.buildTree(
            preorder[1 + left_count :], inorder[root_index + 1 :]
        )

        return root


"""
preorder = [3,9,20,15,7]

inorder = [9,3,15,20,7]
             r
"""
