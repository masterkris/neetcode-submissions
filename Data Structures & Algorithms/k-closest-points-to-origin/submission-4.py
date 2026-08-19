class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # closest = min. distance = max. heap

        maxHeap = []

        for x, y in points:
            dist = x**2 + y**2 # from origin
            heapq.heappush_max(maxHeap, [dist, x, y])

            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop_max(maxHeap)
            res.append([x,y])
        
        return res
        