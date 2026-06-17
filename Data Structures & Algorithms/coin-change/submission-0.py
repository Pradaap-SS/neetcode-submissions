class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)   # fill with infinity (impossible)
        dp[0] = 0                             # base case: 0 coins to make amount 0

        for i in range(1, amount + 1):        # for every amount
            for coin in coins:                # try every coin
                if i - coin >= 0:            # valid coin to use?
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1