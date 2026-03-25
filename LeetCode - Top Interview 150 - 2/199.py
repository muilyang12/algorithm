# Time Complexity: O(n), Space Complexity: O(n) -> Worst case
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        result = []

        while queue:
            result.append(queue[-1].val)

            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


"""
I solved this using the BFS approach. I used the method I learned from a lady at my previous study group. However, I heard that this problem can also be solved using DFS. The idea is to pass the depth
as an argument when calling the `dfs` function. Then, you compare the current node's depth with the current length of the result list. If it's the first time being called at that specific depth, it 
must be the rightmost value. For this to work, you need a rule to call both the left and right children, but you must call the right child first.
"""
