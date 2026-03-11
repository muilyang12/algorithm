# Time Complexity: O(V + E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree_list = [0 for _ in range(numCourses)]
        for after, before in prerequisites:
            graph[before].append(after)
            indegree_list[after] += 1

        queue = deque()
        for index, indegree in enumerate(indegree_list):
            if indegree == 0:
                queue.append(index)

        while queue:
            target = queue.popleft()

            for next_node in graph[target]:
                indegree_list[next_node] -= 1

                if indegree_list[next_node] == 0:
                    queue.append(next_node)

        for indegree in indegree_list:
            if indegree != 0:
                return False

        return True


# Time Complexity: O (v^2)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = set()

        for after, before in prerequisites:
            graph[after].add(before)

        zero_indegree_nodes = deque()

        for key in graph:
            if len(graph[key]) == 0:
                zero_indegree_nodes.append(key)

        while zero_indegree_nodes:
            target = zero_indegree_nodes.popleft()

            del graph[target]

            for key in graph:
                if target in graph[key]:
                    graph[key].remove(target)

            for key in graph:
                if len(graph[key]) == 0 and key not in zero_indegree_nodes:
                    zero_indegree_nodes.append(key)

        return True if len(graph) == 0 else False


"""
Number is 0 - (num - 1)?
"""

"""
[[3,2],[3,1],[2,0],[1,0]]

{0: [], 1: [0], 2: [0], 3: [2, 1]}

[0]

{1: [], 2: [], 3: [2, 1]}

[1, 2]
{3: []}

[3]
{}
"""

"""
Edge Case

"""


"""
This is a Topological Sort problem I found in a Glassdoor interview review. It's a must-know. You can solve it using either BFS or DFS. 
The basic idea of the BFS approach is to start with nodes that have an indegree of 0. Once you 'take' a course, you remove it from the 
prerequisite list of its neighbors, which eventually creates new nodes with an indegree of 0. The DFS approach follows a similar logic, 
starting from nodes where the indegree is 0. Ultimately, the goal is to traverse the graph along the arrows and detect if a cycle exists
"""
