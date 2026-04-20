class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 2-pointer approach
        # start both from 0
        # declare max variable
        # iterate and update max variable
        # update pointers depending on whether prices[l] < prices[r]
        # O(n) time, O(1) space

        l,r = 0,1
        maxProf = 0

        while r < len(prices):
            if prices[l] < prices[r]: # want this for profit
                  maxProf = max(maxProf, prices[r] - prices[l])
            else:
                  l = r  # can't have left greater than right, move to at least right
            r += 1
        
        return maxProf




        