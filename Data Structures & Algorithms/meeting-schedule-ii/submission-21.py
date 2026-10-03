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
        # list of objects -> lambda
        # min-heap
        # keep track of first end
        # add interval end times to min_heap
        # check next start time with current latest end time in min_heap and add to min_heap accordingly
        # min_heap stores which rooms are curr. being used
        # once we're done with a meeting, pop from min_heap
        # min. number of rooms = len(min_heap)

        if not intervals:
            return 0

        intervals.sort(key = lambda x: x.start)

        min_heap = []
        first_end = intervals[0].end

        heapq.heappush(min_heap, first_end)

        for i in range(1, len(intervals)):
            if intervals[i].start < min_heap[0]:
                heapq.heappush(min_heap, intervals[i].end)
            else:
                # done with the last room
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, intervals[i].end)
        
        return len(min_heap)





        