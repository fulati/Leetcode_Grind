class Solution:
    def partitionString(self, s: str) -> List[str]:
        
        output = []
        seen = set()

        l, r = 0, 1

        while r < len(s) + 1:

            if s[l:r] not in seen:
                output.append(s[l:r])
                seen.add(s[l:r])
                l = r
            
            r += 1
        
        return output

