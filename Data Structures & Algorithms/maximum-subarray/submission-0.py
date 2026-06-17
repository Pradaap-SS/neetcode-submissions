class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current = nums[0]

        for n in nums[1:]:
            current = max(n, current + n)  # restart if current sum is negative
            max_sum = max(max_sum, current)

        return max_sum