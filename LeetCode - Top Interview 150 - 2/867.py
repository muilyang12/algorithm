class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(len(matrix))] for __ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i] = matrix[i][j]

        return result


"""
[1,2,3]
[4,5,6]
[7,8,9]

=====

[1,2,3]
[4,5,6]

[]
[]
[]
"""
