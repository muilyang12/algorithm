class Node:
    def __init__(self, depth):
        self.is_end = False
        self.next_nodes = {}
        self.depth = depth


class Trie:
    def __init__(self):
        self.head = Node(0)
        self.height = 0

    def insert(self, word: str) -> None:
        current = self.head

        for char in word:
            if char in current.next_nodes: 
                current = current.next_nodes[char]
            else:
                self.height = max(self.height, current.depth + 1)
                current.next_nodes[char] = Node(current.depth + 1)
                current = current.next_nodes[char]
        
        if not current.is_end:
            current.is_end = True

    def search(self, word: str) -> bool:
        if len(word) > self.height:
            return False

        current = self.head

        for char in word:
            if char in current.next_nodes: 
                current = current.next_nodes[char]
            else:
                return False
        
        if not current.is_end:
            return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) > self.height:
            return False

        current = self.head

        for char in prefix:
            if char in current.next_nodes: 
                current = current.next_nodes[char]
            else:
                return False
        
        return True


"""
null
a 
p
p
l
e <
"""