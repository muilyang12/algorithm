class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        def dfs_clone(node, hash):
            if not node:
                return None

            if node in hash:
                return hash[node]

            new_node = Node(node.val)
            hash[node] = new_node

            new_node.next = dfs_clone(node.next, hash)
            new_node.random = dfs_clone(node.random, hash)

            return new_node

        return dfs_clone(head, {})


"""
When I first saw this problem, I was stuck on how to approach it. I knew I had to use a hash map to store the newly created nodes, but I wasn't sure what to use as the key. In the "133. Clone Graph" problem,
the values were unique, so I used the value as the key, but that's not the case here.

After talking with Gemini, it suggested storing them in the hash map as `old_node: new_node`. While using the value worked for the Clone Graph problem, Gemini added that the `old_node: new_node` approach
would have been better even in that case.
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        old_new_map = {}

        def dfs_copy_node(node):
            if not node:
                return None

            if node in old_new_map:
                return old_new_map[node]

            new_node = Node(node.val)
            old_new_map[node] = new_node

            new_node.next = dfs_copy_node(node.next)
            new_node.random = dfs_copy_node(node.random)

            return new_node

        return dfs_copy_node(head)
