class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        cur_max, cur_min = 1,1
        temp = cur_max + 1

        for num in nums:
            if num == 0:
                cur_max, cur_min = 1,1
                continue
            
            temp = cur_max

            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * temp, num * cur_min)

            res = max(res, cur_max)

        return res
        