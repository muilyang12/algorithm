class Node:
    def __init__(self, char, depth):
        self.char = char
        self.is_end = False
        self.next_nodes = {}
        self.depth = depth


class WordDictionary:
    def __init__(self):
        self.head = Node(None, 0)
        self.height = 0

    def addWord(self, word: str) -> None:
        current = self.head

        for char in word:
            if not char in current.next_nodes:
                self.height = max(self.height, current.depth + 1)
                current.next_nodes[char] = Node(char, current.depth + 1)
                current = current.next_nodes[char]
            else:
                current = current.next_nodes[char]

        current.is_end = True

    def search(self, word: str) -> bool:
        if (len(word) > self.height):
            return False

        current = self.head

        return self._dfs_search(word, current)

    def _dfs_search(self, word_part, temp_head):
        current = temp_head

        for index, char in enumerate(word_part):
            if char in current.next_nodes:
                current = current.next_nodes[char]
            elif char == ".":
                word_part = word_part[index + 1 :]
                for next_node in current.next_nodes.values():
                    dfs_result = self._dfs_search(word_part, next_node)
                    if dfs_result:
                        return True
                return False
            else:
                return False

        if current.is_end:
            return True
        else:
            return False


"""
null
b // d < // m
a // a // a
d // d // d

1. pad
index, char
0, p -> False

2. bad
index, char
0, b
1, a
2, d
-> True

3. .ad
index, char
0, .

3' ad
index, char
0, a
1, d
-> True

3'' ad
"""

"""
addWord: [["a"],["a"]]
search: [["."],["a"],["aa"],["a"],[".a"],["a."]]

null
a <

a.
index, char
0, a
1, .
"""

"""
Edge Cases
Empty
Height > Search Word Length
Height < Search Word Length

[] ["a"] // ["a"] [""]
["aaa"] ["a"] -> False
["a"] ["aaa"] -> False
"""
