class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, open_count, close_count): 
            
            if open_count == close_count == n:
                res.append(curr)
                return
            
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res