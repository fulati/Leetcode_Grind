class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row = 0
        going_down = False

        for c in s:
            rows[cur_row] += c

            if cur_row == 0:
                step = 1
                
            elif cur_row == numRows - 1:
                step = -1
            
            cur_row += step

        return "".join(rows)