class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        self.graph = {}

        for i in range(len(equations)):
            first, second = equations[i]
            value = values[i]

            if first not in self.graph:
                self.graph[first] = []
            if second not in self.graph:
                self.graph[second] = []

            self.graph[first].append((second, value))
            self.graph[second].append((first, 1 / value))

        result = [self.dfs_calculate(query[0], query[1], 1, set()) for query in queries]

        return result

    def dfs_calculate(self, start_char, end_char, current=1, visited=set()):
        if start_char not in self.graph:
            return -1

        if start_char == end_char:
            return current

        visited.add(start_char)

        for next_char, next_value in self.graph[start_char]:
            if next_char in visited:
                continue

            result = self.dfs_calculate(
                next_char, end_char, current * next_value, visited
            )

            if result > 0:
                return result

        visited.remove(start_char)

        return -1


"""
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]

graph = {
    "a": [("b", 2)]
    "b": [("a", 0.5), ("c", 3)]
    "c": [("b", 0.33333)]
}

queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
                                 ^
"""

"""
The condition for identifying a graph problem is when relationships between various values are given, such as A to B, B to C, and C back to A. This was the case with the relationship
between accounts and emails in "721. Accounts Merge", the multiplicative relationships between characters here, and the ordering of classes in "210. Course Schedule II". Once you
realize the problem should be solved using a graph and manage to build the graph dictionary, you have already completed half the work. From that point on, it is just a matter of DFS
traversal, which is quite familiar.
"""
