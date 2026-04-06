"""
This problem is quite unique. The core concept is exactly the same as the House Robber problem, but the houses are arranged in a Binary Tree instead of an array. It seems like I could just create a memo tree,
just as I would create a memo array for the array-based version. However, there is a problem. With a memo array, I can easily access values using indices, but since this is a tree, accessing the values of
previous nodes within a memo tree is a bit difficult.

After talking with Gemini, it suggested a clever approach. Since DFS travels all the way down and then comes back up, and we have to move in both directions anyway, the idea was to collect the values while
moving up the tree instead of trying to do it while going down. I think this is a great method to keep in mind.
"""

"""
This one is really tough. I definitely need to remember the approach of using `with_node` and `without_node`, especially the logic behind calculating the `without_node` value.
"""


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs_get_max_profit(node):
            if not node:
                return (0, 0)

            with_left, without_left = dfs_get_max_profit(node.left)
            with_right, without_right = dfs_get_max_profit(node.right)

            with_node = without_left + without_right + node.val
            without_node = max(with_left, without_left) + max(with_right, without_right)

            return (with_node, without_node)

        with_root, without_root = dfs_get_max_profit(root)

        return max(with_root, without_root)


"""
3

2   3

X 3 x 1

DFS returns (current 포함, current 안 포함)
"""
