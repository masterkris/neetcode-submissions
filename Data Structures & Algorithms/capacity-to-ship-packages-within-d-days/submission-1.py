class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)
        res = r

        while l <= r:
            k = (l + r) // 2

            total = 1
            current = 0

            for weight in weights:
               if current + weight > k:
                  total += 1
                  current = weight
               else:
                  current += weight

            if total <= days:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
            

        