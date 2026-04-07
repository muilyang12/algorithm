class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # depth_size = min(matrix, matrix[0]) // 2 + (1 if odd else 0)

        # for depth in (depth_size)
        #     for i == depth
        #     for j == len - depth
        #     for i == len - depth
        #     for j = depth
