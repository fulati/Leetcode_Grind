class Solution:
    def isValid(self, s: str) -> bool:
        store = {"}":"{", ")":"(", "]":"["}

        stack = []

        for c in s: 
            
            if c in store:

                if stack and store[c] == stack[-1]: 
                        stack.pop()
                else: 
                    return False

            else:
                stack.append(c)

        return len(stack) == 0