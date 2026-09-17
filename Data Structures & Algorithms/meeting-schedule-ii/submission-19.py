"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # sort by start time
        # store first end
        # when we see one overlap, we start a new room and update the previous end

        if not intervals:
            return 0

        intervals.sort(key = lambda x: x.start)
        curr_ends = []
        heapq.heappush(curr_ends, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= curr_ends[0]:
                heapq.heappop(curr_ends)
            heapq.heappush(curr_ends, intervals[i].end)
        
        return len(curr_ends)
        