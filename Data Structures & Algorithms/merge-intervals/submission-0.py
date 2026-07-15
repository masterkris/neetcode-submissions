class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Plan --> 
        # Sort intervals list first
        # declare res list
        # iterate through intervals
        # [1,3] + [1,5] = [1, 5], so if intervals[-1][1] >= intervals[0][1], append to result
        # else add both

        intervals.sort()

        res = []

        for i in range(1, len(intervals)):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i][0] = intervals[i-1][0]
                intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
            else:
                res.append(intervals[i - 1])
        
        res.append(intervals[len(intervals) - 1])
        
        return res