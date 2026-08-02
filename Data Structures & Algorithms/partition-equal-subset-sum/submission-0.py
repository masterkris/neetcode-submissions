class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # to partition, has to be even
        # check if sum % 2 == 0, else return false
        # declare target = sum // 2
        # dp = [target + 1] * [False]
        # set dp[0] = True
        # for each num in nums:
        # traverse j backwards from target to num - 1
        # update dp[j] = dp[j] OR dp[j - num]
        # could I already make sum j or can I make it now?
        # knapsack DP pattern
        # dp[j] -- can i make sum j? target is half total  sum
        # return dp[target]

        n = sum(nums)

        if n % 2 != 0:
            return False
        
        target = n // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]
        