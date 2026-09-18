class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # hashmap -> frequency
        # add to an array
        # top k -> heap

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for val in count:
            heapq.heappush(heap, (count[val], val))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        