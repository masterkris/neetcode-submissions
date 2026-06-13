class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # make all stones -ve and build heap --> makes maxheap
        # or we can use the new maxheap functionality
        # pop two smallest/heaviest stones (max-heap)
        # run simulation
        # when 0 or 1 stones remaining, return

        heapq.heapify_max(stones)

        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            if first > second:
                heapq.heappush_max(stones, first - second)
            

        return stones[0] if stones else 0
        