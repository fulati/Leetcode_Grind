class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])

        def dfs(r, c, k):

            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]: 
                return False
            
            if k == len(word) - 1:
                return True            

            temp = board[r][c]

            board[r][c] = "#"

            found = (dfs(r - 1, c, k + 1) or 
            dfs(r + 1, c, k + 1) or 
            dfs(r, c - 1, k + 1) or 
            dfs(r, c + 1, k + 1)
            )

            board[r][c] = temp
            return found


        for i in range(m):
            for j in range(n):

                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False