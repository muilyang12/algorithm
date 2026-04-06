class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def dfs_construct(row_start, row_end, col_start, col_end):
            if row_start == row_end and col_start == col_end:
                return Node(grid[row_start][col_start], True)

            count = (row_end - row_start + 1) // 2

            top_left = dfs_construct(
                row_start, row_start + count - 1, col_start, col_start + count - 1
            )
            top_right = dfs_construct(
                row_start, row_start + count - 1, col_start + count, col_end
            )
            bottom_left = dfs_construct(
                row_start + count, row_end, col_start, col_start + count - 1
            )
            bottom_right = dfs_construct(
                row_start + count, row_end, col_start + count, col_end
            )

            if (
                top_left.val == top_right.val == bottom_left.val == bottom_right.val
                and top_left.isLeaf
                and top_right.isLeaf
                and bottom_left.isLeaf
                and bottom_right.isLeaf
            ):
                return Node(grid[row_start][col_start], True)

            current = Node(1, False)

            current.topLeft = top_left
            current.topRight = top_right
            current.bottomLeft = bottom_left
            current.bottomRight = bottom_right

            return current

        return dfs_construct(0, len(grid) - 1, 0, len(grid[0]) - 1)


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def dfs_construct_quad(start_row, end_row, start_col, end_col):
            if start_row == end_row and start_col == end_col:
                return Node(grid[start_row][start_col], 1)

            num_rows = end_row - start_row + 1
            new_end_row = start_row + num_rows // 2 - 1
            num_cols = end_col - start_col + 1
            new_end_col = start_col + num_cols // 2 - 1

            topLeft = dfs_construct_quad(start_row, new_end_row, start_col, new_end_col)
            topRight = dfs_construct_quad(
                start_row, new_end_row, new_end_col + 1, end_col
            )
            bottomLeft = dfs_construct_quad(
                new_end_row + 1, end_row, start_col, new_end_col
            )
            bottomRight = dfs_construct_quad(
                new_end_row + 1, end_row, new_end_col + 1, end_col
            )

            if (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val) and (
                topLeft.isLeaf
                == topRight.isLeaf
                == bottomLeft.isLeaf
                == bottomRight.isLeaf
                == 1
            ):
                return Node(topLeft.val, topLeft.isLeaf)
            else:
                node = Node(1, 0)

                node.topLeft = topLeft
                node.topRight = topRight
                node.bottomLeft = bottomLeft
                node.bottomRight = bottomRight

                return node

        return dfs_construct_quad(0, len(grid) - 1, 0, len(grid[0]) - 1)


"""
[1,1,0,0]
[0,0,1,1]
[1,1,0,0]
[0,0,1,1]
"""
