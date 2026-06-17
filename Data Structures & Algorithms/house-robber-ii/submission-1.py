class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        def rob1(nums):
            prev1, prev2 = 0,0
            for num in nums:
                curr = max( num + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1

        if (len(nums) == 1):
            return nums[0]

        return max(rob1(nums[:-1]),  # exclude last house
                rob1(nums[1:]))       # exclude first house