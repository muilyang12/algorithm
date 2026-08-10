class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        hash = {}

        def dfs(node):
            nonlocal hash

            if not node:
                return

            if node in hash:
                return hash[node]

            new_node = Node(node.val)
            hash[node] = new_node

            new_node.next = dfs(node.next)
            new_node.random = dfs(node.random)

            return new_node

        return dfs(head)
