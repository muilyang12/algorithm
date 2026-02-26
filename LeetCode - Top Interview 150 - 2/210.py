class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        graph = {}

        for i in range(numCourses):
            graph[i] = set()

        for des, ori in prerequisites:
            graph[des].add(ori)

        while True:
            zero_indegree_nodes = [
                from_node for from_node, to_nodes in graph.items() if len(to_nodes) == 0
            ]

            if len(zero_indegree_nodes) == 0 and len(graph) != 0:
                return []

            if len(zero_indegree_nodes) == 0 and len(graph) == 0:
                return result

            for target in zero_indegree_nodes:
                result.append(target)

                del graph[target]

                for to_nodes in graph.values():
                    if target in to_nodes:
                        to_nodes.remove(target)


"""
numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]

{
0: []
1: [0]
2: [0]
3: [1, 2]
}


zero_indegree_nodes = [0]

0 - 1 - 3
  \ 2 /

Indegree

=====

numCourses = 1, prerequisites = []

{
0: []
}

zero_indegree_nodes = [0]
"""
