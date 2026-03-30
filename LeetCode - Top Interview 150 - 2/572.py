# Time Complexity: O(n + m) or O(nm), Space Complexity: O(n + m)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs_is_same_tree(original_node, node_to_compare):
            if not original_node and not node_to_compare:
                return True
            elif not original_node or not node_to_compare:
                return False
            elif original_node.val != node_to_compare.val:
                return False
            else:
                return dfs_is_same_tree(
                    original_node.left, node_to_compare.left
                ) and dfs_is_same_tree(original_node.right, node_to_compare.right)

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and dfs_is_same_tree(node, subRoot):
                return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False


"""
Same number can exist?
"""

"""
Using it this way allows you to cover the case where only one node is `one` with a short if statement.

`if not original_node and not node_to_compare:`

`elif not original_node or not node_to_compare:`
"""

"""
Calculating the complexity for this problem is quite tricky.

1. For the Time Complexity, the ideal scenario would be encountering a node in the root tree that matches the value of the subRoot and finding that they are identical. 
In such a case, the complexity would be O(n + m). However, the worst-case scenario occurs when nodes with the same value appear repeatedly, and the overall tree
structure remains very similar. In that situation, the time complexity could degrade to O(nm), which is not very efficient.
2. As for the Space Complexity, we must account for both the space occupied by the queue during traversal and the space used by the DFS recursion stack. Therefore, it
would be O(n + m).
"""


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
