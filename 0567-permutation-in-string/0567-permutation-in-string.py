class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = defaultdict(int)
        s2Dict = defaultdict(int)

        for i in range(len(s1)): 
            s1Dict[s1[i]] += 1

        l = 0

        for r in range(len(s2)):
            
            s2Dict[s2[r]] += 1

            if r - l + 1 > len(s1):
                s2Dict[s2[l]] -= 1

                if s2Dict[s2[l]] == 0:
                    del s2Dict[s2[l]]
                
                l += 1
                
            if s1Dict == s2Dict:
                return True

        return False