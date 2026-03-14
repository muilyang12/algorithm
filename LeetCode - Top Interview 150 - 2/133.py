class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        node_map = {}

        def clone_node(target_node):
            if not target_node:
                return None

            if target_node.val in node_map:
                return node_map[target_node.val]

            new_node = Node(target_node.val)
            node_map[target_node.val] = new_node

            for n in target_node.neighbors:
                new_node.neighbors.append(clone_node(n))

            return new_node

        return clone_node(node)


"""
Value unique?
"""

"""
I've solved this type of problem many times. The key is to cache each node in a map immediately after creating it, so I can reuse it later for faster performance. To do this,
I needed a unique identifier for each node. I asked myself, 'Is the value unique?' This line of reasoning was very effective.
"""