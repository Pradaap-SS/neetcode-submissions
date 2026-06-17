class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0        # dp[i-2], dp[i-1]

        for num in nums:
            current = max(num + prev2, prev1)  # rob it vs skip it
            prev2 = prev1
            prev1 = current

        return prev1