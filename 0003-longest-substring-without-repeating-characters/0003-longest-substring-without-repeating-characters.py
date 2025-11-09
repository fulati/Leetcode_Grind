class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        substr = set()

        l, r = 0, 0

        while r < len(s): 

            while s[r] in substr: 
                substr.remove(s[l])
                l += 1
            
            substr.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest 