class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # [1, 4, 3, 2]
        # hours: 1, 2, 2, 1
        # 6 hrs < 9 hrs

        l = 1
        r = max(piles) # 4 in example above, 4 is max

        res = r # max in piles

        while (l <= r):
            k = (l + r) // 2  # 2 for example above

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k) # account for remainders
                # 6 hrs <= 9 hrs --> update res
            
            if hours <= h:
                res = min(res, k)
                r = k - 1 # check for smaller speed
            else:
                l = k + 1

        return res





        