class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row_set = set()
            col_set = set()
            part_set = set()

            for j in range(len(board)):
                if board[i][j] in row_set:
                    return False
                elif board[i][j] != ".":
                    row_set.add(board[i][j])

                if board[j][i] in col_set:
                    return False
                elif board[j][i] != ".":
                    col_set.add(board[j][i])

                part_target = board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3]
                if part_target in part_set:
                    return False
                elif part_target != ".":
                    part_set.add(part_target)

        return True
