class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D DP table with all 1s
        dp = [[1] * n for _ in range(m)]

        # Fill in the table bottom-up
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m-1][n-1]