class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for i in range(numCourses):
            graph[i] = set()

        for target, prerequisite in prerequisites:
            graph[prerequisite].add(target)

        while True:
            zero_indegree_nodes = [from_node for from_node, to_nodes in graph.items() if len(to_nodes) == 0]

            if len(zero_indegree_nodes) == 0 and len(graph) == 0:
                return True
            elif len(zero_indegree_nodes) == 0 and len(graph) != 0:
                return False

            for target in zero_indegree_nodes:
                del graph[target]

                for to_nodes in graph.values():
                    if target in to_nodes:
                        to_nodes.remove(target)

"""
numCourses = 2, prerequisites = [[1,0],[0,1]]

{
0: [1]
1: []
}
"""