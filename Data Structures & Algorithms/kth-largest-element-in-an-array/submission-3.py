class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # can use max-heap
        # iterate through nums and add the nums to a max-heap
        # pop k elements until we return kth largest

        # optimize: use min-heap
        # push into min_heap, pop if greater than k
        # kth largest will be at top

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
        

        
        