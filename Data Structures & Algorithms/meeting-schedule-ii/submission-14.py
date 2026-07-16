"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # similar to meeting rooms I except we need to keep track of how many rooms
        # sort using lambda
        # store end_1 in a variable (curr_end)
        # declare rooms variable
        # iterate from 1 to len(intervals)
        # at any point, if the start of the interval is less than curr_end, increment rooms by 1
        # if we do end up forming a new room, we update curr_end to the new_end

        if not intervals:
            return 0 

        intervals.sort(key = lambda x: x.start)

        # min-heap (by default) to track which room becomes available first
        curr_ends = []
        heapq.heappush(curr_ends, intervals[0].end) # add first end

        # rooms = 1 # need at least 1 room to begin with

        for i in range(1, len(intervals)):
            if intervals[i].start >= curr_ends[0]: # room is free
                heapq.heappop(curr_ends)

                # [10, 40]
                # 15 > 10, 10 is done using. pop
                # [15, 40]

            # we need to put this room into existing OR book new room
            heapq.heappush(curr_ends, intervals[i].end)
        
        return len(curr_ends)

        