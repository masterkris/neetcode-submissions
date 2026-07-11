class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # [1, 2, 3] 0
        
        for i in range(len(cost) - 3, -1, -1):
            # range(start, stop, step)

            cost[i] += min(cost[i + 1], cost[i + 2])

        
        return min(cost[0], cost[1]) # cost starting at 0 vs 1