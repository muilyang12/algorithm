class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(head1, head2):
            if not head1 and not head2:
                return True

            if head1 and not head2:
                return False
            if not head1 and head2:
                return False
            if head1.val != head2.val:
                return False

            return is_same_tree(head1.left, head2.left) and is_same_tree(
                head1.right, head2.right
            )

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.val == subRoot.val:
                if is_same_tree(node, subRoot):
                    return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False
