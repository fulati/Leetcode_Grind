class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        sqr_dict = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in row_dict[i] or board[i][j] in col_dict[j] or board[i][j] in sqr_dict[i//3, j//3]:
                    return False

                row_dict[i].add(board[i][j])
                col_dict[j].add(board[i][j])
                sqr_dict[i//3, j//3].add(board[i][j])
            
        return True