"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # sort the intervals list by start time
        # not lists, time interval objects, so need to sort using lambda
        # can use .start and .end
        # store last element of first interval in list (currLast)

        # iterate through list (1 -> end)
        # compare first element to the currLast. if first element < currLast, return False immediately
        # return True at end

        if not intervals:
           return True

        intervals.sort(key = lambda x: x.start)

        currLast = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < currLast:
                return False
            currLast = max(currLast, intervals[i].end)
        
        return True
