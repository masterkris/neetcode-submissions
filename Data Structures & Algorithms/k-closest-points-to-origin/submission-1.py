class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []  # want to pop k from end and return, so max

        for x, y in points:
            dist = (x ** 2 + y ** 2) # don't need square root, this accounts for distance
            heapq.heappush_max(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
            
        res = []
        while (k > 0):
            dist, x, y = heapq.heappop_max(maxHeap)
            heapq.heappush_max(res, [x, y])
            k -= 1

        return res

        