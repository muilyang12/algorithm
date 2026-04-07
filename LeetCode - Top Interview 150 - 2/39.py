class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []

        def dfs_comb_sum(temp, strart, current_sum):
            if current_sum > target:
                return
            elif current_sum == target:
                self.result.append(temp[:])
                return

            for i in range(strart, len(candidates)):
                num = candidates[i]

                temp.append(num)
                dfs_comb_sum(temp, i, current_sum + num)
                temp.pop()

        dfs_comb_sum([], 0, 0)

        return self.result


"""
The idea of placing the coin loop on the outside in the Coin Change problem ensures that you cannot use any elements prior to the current index. This effectively results in a combination rather than a permutation.
Here, you can achieve the exact same effect by passing a starting index as a parameter to the function. This ensures that the recursion only explores the current and subsequent elements, preventing the algorithm
from looking back at previous values.
"""
