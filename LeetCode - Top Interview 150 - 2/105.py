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
