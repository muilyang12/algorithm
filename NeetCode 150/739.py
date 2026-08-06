class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]

        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            temp = temperatures[i]

            while stack and stack[-1][0] < temp:
                _, index = stack.pop()

                result[index] = i - index

            stack.append((temp, i))

        return result
