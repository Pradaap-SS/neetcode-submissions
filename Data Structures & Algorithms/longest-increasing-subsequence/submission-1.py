class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)        # every element is LIS of length 1 alone

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:               # strictly increasing?
                    dp[i] = max(dp[i], dp[j] + 1)  # extend the subsequence

        return max(dp)