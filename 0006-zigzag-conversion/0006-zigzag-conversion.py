class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows >= len(s) or numRows == 1:
            return s

        output = [""] * numRows
        cur_row = 0

        for c in s:
            output[cur_row] += c

            if cur_row == 0:
                t = 1
            elif cur_row == numRows - 1:
                t = -1
            
            cur_row += t

        return "".join(output)
