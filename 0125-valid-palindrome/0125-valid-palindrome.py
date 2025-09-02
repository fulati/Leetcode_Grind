class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ""

        for c in s:
            if c.isalnum():
                output += (c.lower())
        
        return output == output[::-1]