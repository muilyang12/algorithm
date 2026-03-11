class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree_list = [0 for i in range(numCourses)]

        for after, before in prerequisites:
            graph[before].append(after)
            indegree_list[after] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree_list[i] == 0:
                queue.append(i)

        result = []
        while queue:
            target = queue.popleft()
            result.append(target)

            for after in graph[target]:
                indegree_list[after] -= 1
                if indegree_list[after] == 0:
                    queue.append(after)

        for indegree in indegree_list:
            if indegree != 0:
                return []

        return result


"""
I solved this problem using BFS as well, but with a more optimized approach than before. Instead of traversing the entire `graph` every time to find nodes
with `indegree == 0`, I maintained an indegree_list array. By looking up and updating this array, I was able to reduce the overall time complexity to O(V + E).
"""
