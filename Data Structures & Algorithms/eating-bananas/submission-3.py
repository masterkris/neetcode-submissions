class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # [1, 4, 3, 2]
        # define possible ans. search range

        # l = min. possible ans.
        # r = max. possible ans.

        # find mid while l <= r
        # if mid works, try smaller
        # if doesn't work, try bigger
        # return left

        l = 1
        r = max(piles)
        res = r # start from max

        while l <= r:
            k = (l + r) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h: # satisfies condition
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
            

        