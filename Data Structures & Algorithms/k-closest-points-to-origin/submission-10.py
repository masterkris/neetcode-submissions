class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

       # closest points = maxHeap

       # push distances from the origin to each point to maxHeap
       # keep track of the coordinates and distance for each
       # so we can return coordinates at the end
       # if length > k, pop from heap
       # add the k closest points to a res list
       # return

       maxHeap = []
       
       for x, y in points:
           distance = x**2 + y**2
           heapq.heappush_max(maxHeap, [distance, x, y])

           if len(maxHeap) > k:
              heapq.heappop_max(maxHeap)
        
       res = []

       for i in range(k):
            dist, x, y = heapq.heappop_max(maxHeap)
            res.append([x,y])
        
       return res

        
        