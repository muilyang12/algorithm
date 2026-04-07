"""
graph = {before: [after]}
indegree_counts = [0 for num_nodes]
indegree_counts[after] += 1

indegree_counts[i]: Count of nodes pointing node i

when indegree_counts[i] == 1, put it in queue

while queue:
    for graph[target]
        indegree -= 1

        if == 0, append in the queue

if indegree > 0, there is a cycle
"""


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


"""
This problem can be solved with both BFS and DFS. Even within BFS, there's a faster approach compared to my initial implementation.

While both use a queue and a while loop, the key difference lies in how they identify zero-indegree nodes. The faster method maintains an indegree_list array 
and checks for zero values in O(1) time. In contrast, my initial approach directly modifies the graph and counts remaining elements during each cycle. This is
why the approach using `indegree_list` is much more efficient,

It’s fascinating how the time complexity is calculated as O(V + E). Since every vertex enters the queue exactly once, the while-loop runs V times. More
importantly, regardless of how many times the while loop iterates, every edge is visited exactly once across the for-loop. Because the total number of for loop
iterations is fixed by the number of edges, the complexity is O(V + E) rather than O(VE).
"""


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
