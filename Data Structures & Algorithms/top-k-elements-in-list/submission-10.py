class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        min_heap = []

        for val in count:
            heapq.heappush(min_heap, [count[val], val])

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []
        while k > 0:
            freq, val = heapq.heappop(min_heap)
            res.append(val)
            k -= 1
        
        return res
        