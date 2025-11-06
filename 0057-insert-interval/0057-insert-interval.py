class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []

        start, end = newInterval

        for s, e in intervals:

            if start > e: 
                output.append([s,e])
            elif end < s:
                output.append([start, end])
                start = s
                end = e
            else: 
                start = min(start, s)
                end = max(end, e)
        
        output.append([start, end])
        
        return output