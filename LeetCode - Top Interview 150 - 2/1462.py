class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        memo = [[None for _ in range(numCourses)] for __ in range(numCourses)]
        for i in range(numCourses):
            memo[i][i] = True

        prerequisite_graph = {i: [] for i in range(numCourses)}
        for before, after in prerequisites:
            prerequisite_graph[after].append(before)
            memo[before][after] = True

        result = []
        for before, after in queries:
            current_result = self.dfs_check_if_prerequisite(
                prerequisite_graph, before, after, set(), memo
            )
            if memo[before][after] == None:
                memo[before][after] = current_result

            result.append(current_result)

        return result

    def dfs_check_if_prerequisite(
        self, prerequisite_graph, before, after, visited, memo
    ):
        if memo[before][after] != None:
            return memo[before][after]

        if before == after:
            return True

        visited.add(after)

        for prerequisite in prerequisite_graph[after]:
            if prerequisite in visited:
                continue

            result = self.dfs_check_if_prerequisite(
                prerequisite_graph, before, prerequisite, visited, memo
            )
            if memo[before][prerequisite] == None:
                memo[before][prerequisite] = result

            if result:
                return True

        visited.remove(after)

        return False


"""
This problem is truly difficult. It beautifully harmonizes the two concepts of Graph (using DFS) and Dynamic Programming.

The conventional approach performs a complete DFS for every single query, resulting in a time complexity of O(q (v + e))
"""

"""
In Course Schedule I, we only check for the existence of cycles. In Course Schedule II, we just need to find a single valid ordering. However, this problem, Course Schedule IV,
provides multiple queries and requires us to determine if a prerequisite relationship exists for each of them. If we solved this naively, we would perform a DFS for every single
query. But that would lead to an excessively high time complexity of O(q (v + e)), making a simple DFS impractical. That is why a DP-style approach is added to the solution. The
fundamental difference between these problems lies in how many times you must traverse the DFS.

I have noted several times when to update the `visited` set in BFS problems. A similar mindset is required here as well. Whether it is a `visited` set or a `memo` table, updating
it as early as possible is advantageous for runtime because it prevents unnecessary calls. Therefore, instead of updating the `memo` only after receiving the final value from the
DFS function, you should continuously update the `memo` every time a DFS is invoked within the function.
"""

"""
I initially thought the time complexity of performing a DFS for every query was O(qn). However, both Gemini and the official solutions state that O(q (v + e)) is a more accurate
representation. They explained that in graph problems, it is fundamentally correct to express the time complexity of DFS or BFS as O(v + e). This is an important point to remember.
"""
