class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        result = []

        while queue:
            current_result = []

            current_level_count = len(queue)
            for _ in range(current_level_count):
                target_node = queue.popleft()
                current_result.append(target_node.val)

                if target_node.left:
                    queue.append(target_node.left)
                if target_node.right:
                    queue.append(target_node.right)

            result.append(current_result)

        return result
