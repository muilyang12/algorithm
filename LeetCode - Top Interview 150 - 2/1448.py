class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs_search(node, max_so_far):
            if not node:
                return 0

            count = 0

            count += dfs_search(node.left, max(max_so_far, node.val))
            count += dfs_search(node.right, max(max_so_far, node.val))

            if node.val >= max_so_far:
                count += 1
            
            return count

        return dfs_search(root, -math.inf)


"""
I like the approach of finding Good Nodes using `max_so_far`. However, using the nonlocal keyword to directly modify a value outside the `dfs` function felt a bit off to me. I had a brief chat
with Gemini about this, and it suggested an alternative. It said like how about having the function return the current count instead?

There are two key takeaways from this problem
1. While passing the `path` works, passing `max_so_far` is even better. This idea is similar to the approach used in problems like "Best Time to Buy and Sell Stock" or "Trapping Rain Water."
2. Let's aim to design `dfs` functions so that they return something like a Node or a value. It feels like this opens up many more possibilities.
"""


"""
But I didn't handle this problem very well. It's because when I first called the `dfs_search` function, I carelessly set the `max_so_far` value to 0. I shouldn't just make assumptions in my head.
I should always ask questions and communicate. I should have asked a question during that process especially about the minimum possible value that could be in a node. If there's an assumption
that values are positive, starting at -1 or 0 would be fine. But that wasn't the case, right? In that situation, I should have started from negative infinity. You know that proceeding without
checking these details is a really bad signal, right? I need to be careful.
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs_search(node, max_so_far):
            nonlocal count

            if not node:
                return

            if node.val >= max_so_far:
                count += 1

            dfs_search(node.left, max(max_so_far, node.val))
            dfs_search(node.right, max(max_so_far, node.val))

        dfs_search(root, -math.inf)

        return count


"""
Since I've used the method of storing and accumulating paths a few times for this type of problem, I initially used the approach shown below, passing the `path` and recording everything visited
until reaching the current node. Of course, if I use a path like this, I'll have to push and pop, right? In this case, the Space Complexity would be O(log n) for a balanced tree, but in the worst
case, it could grow up to O(n). So, it's not very efficient.

Gemini suggested that I try passing only the `max_value`. Especially since a node is a "Good Node" if its current value is greater than the maximum of all values encountered so far. So, the idea
is to just keep passing down the maximum value from the root to the current point. Haven't we seen this type of problem quite often?
"""


# Time Complexity: O(nh), O(n^2) at worst, Space Complexity: O(h), O(log n), O(n) at worst
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs_search(node, path):
            nonlocal count

            if not node:
                return

            for i in range(len(path)):
                if path[i].val > node.val:
                    break

                if i == len(path) - 1:
                    count += 1

            path.append(node)
            dfs_search(node.left, path)
            dfs_search(node.right, path)
            path.pop()

        if root:
            count += 1
        dfs_search(root, [])

        return count
