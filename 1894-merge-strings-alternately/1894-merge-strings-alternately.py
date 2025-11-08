class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        output = ""

        for i in range(min(len(word1), len(word2))):
            output += word1[i] + word2[i]
        
        if len(word1) > len(word2):
            output += word1[len(word2):]
        else: 
            output += word2[len(word1):]
        
        return output 