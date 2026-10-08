class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[i] = fewest coins to make amount i
        # dp[i] = min(dp[i], 1 + dp[i-c])

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # make 0 using 0 coins

        for amount in range(amount + 1):
            for coin in coins:
                if amount - coin >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])
        
        if dp[amount] == amount + 1:
            return -1
        
        return dp[amount]


        