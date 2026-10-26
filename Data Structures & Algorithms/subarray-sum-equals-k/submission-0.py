class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # no sliding window here as we have negative numbers

        # keep track of count and sum
        # map prefix sum -> how many times we've seen
        # seen = {0 : 1} --> dictionary

        # iterate through nums
        # add to running sum
        # if (sum - k) exists in seen, then we add to count
        # then increment seen[sum] by 1
        # O(n) time, O(n) space

        count = 0
        sum = 0

        seen = {0 : 1}

        for num in nums:
            sum += num

            if (sum - k) in seen:
                count = count + seen[sum - k]
            
            seen[sum] = 1 + seen.get(sum, 0)
        
        return count

        