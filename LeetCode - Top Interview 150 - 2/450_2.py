class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs_delete_target(node, key):
            if not node:
                return None

            if key > node.val:
                node.right = dfs_delete_target(node.right, key)
            elif key < node.val:
                node.left = dfs_delete_target(node.left, key)
            else:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    target = node.right
                    while target.left != None:
                        target = target.left

                    node.val = target.val
                    node.right = dfs_delete_target(node.right, target.val)

            return node

        return dfs_delete_target(root, key)
