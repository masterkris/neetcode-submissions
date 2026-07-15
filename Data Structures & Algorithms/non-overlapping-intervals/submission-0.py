class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Plan (Algorithm): 
        # sort by start time (regular sort)
        # initialize res = 0
        # set first end (that we will compare to) as intervals[0][1]
        # iterate through intervals
        # we want a common point, so if the current interval's first point is >= the first end, then no overlap
        # in this case, update first end to current end

        # else overlap, increment res and keep the interval with smaller end
        # return res

        # Implementation

        intervals.sort()

        res = 0

        firstEnd = intervals[0][1] # [1,2]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= firstEnd: # no overlap
                firstEnd = intervals[i][1]
            else: # overlap
                res += 1
                firstEnd = min(firstEnd, intervals[i][1]) # if same, stays same
        
        return res





        