class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # can use min-heap
        # iterate through nums and add the nums to a min-heap
        # pop k elements until we return kth largest

        max_heap = []

        for num in nums:
            heapq.heappush_max(max_heap, num)
        
        while k > 1:
            heapq.heappop_max(max_heap)
            k -= 1
        
        return heapq.heappop_max(max_heap)
        

        
        