"""
This reminds me of a recent NeetCode video where he reflected on an interview he took in the past. In that video, he expressed regret because he tried to avoid using global variables
without even checking with the interviewer, even though doing so would have made the problem much easier to solve. This problem might be the very one he was talking about.
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = -math.inf

        def dfs_get_radius(node):
            if not node:
                return 0

            left_radius = dfs_get_radius(node.left)
            right_radius = dfs_get_radius(node.right)

            self.max_diameter = max(self.max_diameter, left_radius + right_radius)

            return max(left_radius, right_radius) + 1

        dfs_get_radius(root)

        return self.max_diameter


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs_get_height_diameter(node):
            if not node:
                return (0, 0)

            left_height, left_max_diameter = dfs_get_height_diameter(node.left)
            right_height, right_max_diameter = dfs_get_height_diameter(node.right)

            current_diameter = left_height + right_height

            max_diameter = max(current_diameter, left_max_diameter, right_max_diameter)

            return (max(left_height, right_height) + 1, max_diameter)

        _, diameter = dfs_get_height_diameter(root)

        return diameter


"""
As you know, solving the problem itself is more important than finding a beautiful solution. Using a path as a parameter in a tree DFS or passing values outside the function using `self.result`
might not be the most elegant approach, but if you cannot think of another way, you should use it. The priority is to solve the problem first.

In this case, you could solve it by continuously updating a maximum value through `self.result` as shown below. However, if you prefer to avoid that, you can take the other approach. This
involves making the DFS function return both the height of the subtree and the maximum diameter found so far.

It is quite interesting to use a method that passes the current maximum diameter while simultaneously returning the height, which acts as a building block for the next node to calculate its
own diameter.

For your information, an advanced version of this problem is "124. Binary Tree Maximum Path Sum".
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.result = 0

        def dfs_get_height(node):
            if not node:
                return 0
            
            left_height = dfs_get_height(node.left)
            right_height = dfs_get_height(node.right)
            current_diameter = left_height + right_height
            
            self.result = max(self.result, current_diameter)

            return max(left_height, right_height) + 1

        dfs_get_height(root)

        return self.result
