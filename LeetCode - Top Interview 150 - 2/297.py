"""
This problem is indeed very difficult. In "662. Maximum Width of Binary Tree," you used the method of putting the index into the queue along with the node during a BFS traversal.
Adopting that same idea allows you to solve this problem relatively easily. Using indices ensures that you can calculate the relative positions and distances between nodes within
the same level without needing to manage a massive amount of None values in your queue.
"""


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


"""
이 아래 방식처럼 None을 계속 넣는 방식은 별로 안 좋아. 왜냐면 가장 오른쪽만 차있는 Skewed의 경우 queue에 None이 2^depth - 1개씩 들어갈텐데 Space complexity의 측면에서 너무 별로잖아.
"""


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
