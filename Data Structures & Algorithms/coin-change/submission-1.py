class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # recurrence: dp[a] = min(dp[a], 1 + dp[a - c])

        # a is amount and c is val. of coin we use

        dp = [amount + 1] * (amount + 1) # store ways to make smaller amounts --> smaller subproblems
        dp[0] = 0   # 0 coins to make 0

        for amount in range(amount + 1):
            for c in coins:
                if amount - c >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - c])
                
        return dp[amount] if dp[amount] != amount + 1 else -1


