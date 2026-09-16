"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # sort by start time
        # iterate through the intervals list
        # if one interval's start time < first interval's start time, immediately return false

        if not intervals:
            return True

        intervals.sort(key= lambda x: x.start)

        first_end = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < first_end:
                return False
            first_end = intervals[i].end
        
        return True
