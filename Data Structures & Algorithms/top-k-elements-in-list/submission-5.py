class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)


        heap = []
        for num in count.keys(): # key -> val (freq)
            heapq.heappush(heap, (count[num], num))

            # if heap exceeds size k, pop least freq. elements
            if len(heap) > k: # min heap -> frequent
                heapq.heappop(heap)
            
        
        res = []

        # now heap contains most frequent, need to get top k freq.
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
