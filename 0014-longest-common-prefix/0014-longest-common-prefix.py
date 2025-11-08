class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest = ""

        for i in range(len(strs[0])):

            ch = strs[0][i]

            for j in range(1, len(strs)):
                
                if i >= len(strs[j]) or ch != strs[j][i]:
                    return longest

            longest += ch
        
        return longest