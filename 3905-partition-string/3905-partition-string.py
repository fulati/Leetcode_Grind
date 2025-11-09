class Solution:
    def partitionString(self, s: str) -> List[str]:
        
        output = []
        s_set = set()
        ch = ''

        for c in s: 

            ch += c

            if ch not in s_set: 
                output.append(ch)
                s_set.add(ch)
                ch = ''
        
        return output