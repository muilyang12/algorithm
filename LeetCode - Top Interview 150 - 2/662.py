class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = -1

        queue = deque()
        queue.append((root, 1))

        while queue:
            first_index, last_index = queue[0][1], queue[-1][1]

            result = max(result, last_index - first_index + 1)

            current_length = len(queue)
            for _ in range(current_length):
                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return result


"""
The way of assigning indices to tree nodes is definitely worth remembering.

While solving this problem, the "297. Serialize and Deserialize Binary Tree" problem kept coming to mind because I had to traverse the tree using BFS and put nodes into a queue.
It felt awkward to decide whether to put None into the queue or how to handle None children of a None node consistently.

The method of putting the node into the queue along with its index is excellent. You should never forget the property that if a current node has an index of `index`, its left
child always has an index of `2 * index` and its right child always has an index of `2 * index + 1`. This indexing method is essential because it allows you to restore the exact
position of a node within the overall tree structure when you pull it back out of the queue.
"""
