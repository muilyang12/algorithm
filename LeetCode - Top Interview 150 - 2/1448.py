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
