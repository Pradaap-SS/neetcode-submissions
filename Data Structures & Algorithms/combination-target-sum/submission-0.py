class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(start, remaining, path):
            # valid combination
            if remaining == 0:
                res.append(path[:])
                return

            # prune invalid path
            if remaining < 0:
                return

            for i in range(start, len(nums)):
                num = nums[i]

                # prune early (since sorted)
                if num > remaining:
                    break

                path.append(num)
                dfs(i, remaining - num, path)  # i again → reuse allowed
                path.pop()

        dfs(0, target, [])
        return res