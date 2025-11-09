class Solution:
    def partitionString(self, s: str) -> List[str]:
        
        output = []
        seen = set()
        cur = ''

        for c in s: 
            
            cur += c

            if cur not in seen: 
                output.append(cur)
                seen.add(cur)
                cur = ''
        
        return output

