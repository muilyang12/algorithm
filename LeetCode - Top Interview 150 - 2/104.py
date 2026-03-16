class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)

        result = 0

        while queue:
            result += 1
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
