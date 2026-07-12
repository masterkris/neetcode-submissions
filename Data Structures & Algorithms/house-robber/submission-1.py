class Solution:
    def rob(self, nums: List[int]) -> int:

        # [rob1, rob2, n, n + 1, n + 2 ...]

        rob1, rob2 = 0, 0
        # rob1 is best up to house i - 2
        # rob2 is best up to house i - 1

        for n in nums:
            curr = max(rob1 + n, rob2)
            # dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            rob1 = rob2
            rob2 = curr
        
        return rob2
        