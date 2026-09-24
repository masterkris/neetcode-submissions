class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals
        # declare res
        # declare firstEnd
        # transform input -> output, then work backward to trace algo
        # [1,2], [1,4], [2,4]
        # [i][0] < firstEnd, res += 1
        # firstEnd stays 2
        # [2,4] --> 2 is not less than 2, new firstEnd is 4

        # if overlap, take min to update firstEnd
        # if no overlap, just update to latest

        intervals.sort()
        res = 0
        firstEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < firstEnd:
                res += 1
                firstEnd = min(firstEnd, intervals[i][1])
            else:
                firstEnd = intervals[i][1]
        
        return res



        