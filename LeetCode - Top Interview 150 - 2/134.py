# Time Complexity O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start_point = 0
        current_point = start_point
        gas_left = 0
        total_distance = 0

        while total_distance < len(gas):
            gas_left += gas[current_point]
            gas_left -= cost[current_point]
            total_distance += 1

            if gas_left < 0:
                gas_left = 0
                total_distance = 0

                start_point = current_point + 1
                current_point = start_point
            else:
                current_point = current_point + 1 if current_point < len(gas) - 1 else 0

        return start_point


"""
[1,2,3,4,5]

[1,3,6,10,15]
[15,2,5,9,14]
[13,15,3,7,12]
"""

"""
Initially, I used nested loops, `for i in range(len(gas))` and `for j in range(i, i + len(gas))`. Conceptually, this is the most standard approach, as it tries to traverse from each starting point `i` 
until it fails. It is a pure Brute Force method. However, this approach has $O(N^2)$ time complexity and resulted in a Time Limit Exceeded.

After discussing with Gemini, it seems this problem requires remembering a specific insight. The core idea is that if I start at `i` and get stuck at `j`, I don't need to check any starting points between
`i` and `j`. During the run from `i`, the gas balance at any point between `i` and `j` was greater than or equal to zero, yet I still couldn't get past `j`. If I start  at one of those intermediate points
with zero gas, I would definitely fail to pass `j` as well.
"""


# Time Complexity O(n^2)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            gas_left = 0

            for j in range(i, i + len(gas)):
                current_j = j if j < len(gas) else j - len(gas)

                gas_left += gas[current_j]
                gas_left -= cost[current_j]

                if gas_left < 0:
                    break

            if gas_left >= 0:
                return i

        return -1
