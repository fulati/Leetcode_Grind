class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        output = []

        intervals.sort(key = lambda x : x[0])

        start, end = intervals[0]

        for i in range(1, len(intervals)):

            s, e = intervals[i]

            if end >= s: 
                end = max(end, e)
            
            else:
                output.append([start, end])
                start, end = intervals[i]

        output.append([start, end])
            
        return output
