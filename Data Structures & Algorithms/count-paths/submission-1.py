class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # dp[i][j] = number of unique paths to point i,j

        dp = [[1] * n for _ in range(m)] # 2D DP arrat

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]