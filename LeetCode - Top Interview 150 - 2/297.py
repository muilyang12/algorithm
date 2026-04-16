class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        result = []

        queue = deque()
        if root:
            queue.append((root, 1))

        while queue:
            node, index = queue.popleft()
            result.append(f"{node.val}|{index}")

            if node.left:
                queue.append((node.left, index * 2))
            if node.right:
                queue.append((node.right, index * 2 + 1))

        return ",".join(result) if result else ""

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        result = None

        hash = {}

        nodes = data.split(",") if data else []

        if nodes:
            value, index = nodes[0].split("|")
            value, index = int(value), int(index)

            result = TreeNode(value)
            hash[index] = result

        for i in range(1, len(nodes)):
            value, index = nodes[i].split("|")
            value, index = int(value), int(index)

            if index % 2 == 0 and index // 2 in hash:
                node = TreeNode(value)
                hash[index // 2].left = node
                hash[index] = node
            elif index % 2 == 1 and (index - 1) // 2 in hash:
                node = TreeNode(value)
                hash[(index - 1) // 2].right = node
                hash[index] = node

        return result
