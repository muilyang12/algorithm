class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs_get_height(node):
            if not node:
                return 0

            return max(dfs_get_height(node.left), dfs_get_height(node.right)) + 1

        return dfs_get_height(root)


"""
When trying to solve this problem using DFS, one approach is to pass the `depth` as a parameter and update a `nonlocal depth` variable. However, I personally dislike using `nonlocal`
for these kinds of solutions.

Of course, there is also the BFS approach, which can solve this problem quite easily as shown in the implementation below.

But since we have been practicing tree traversal in a way where the DFS function returns a value, it seems better to write it that way. In this case, the DFS function would recursively
calculate the heights of the left and right subtrees, add one to the maximum of the two, and then return that value.
"""


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
