class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()      # stores indices
        ans = []

        for r in range(len(nums)):

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            # Add current index
            dq.append(r)

            # Remove indices that are outside the window
            if dq[0] <= r - k:
                dq.popleft()

            # Record the maximum once the window is full
            if r >= k - 1:
                ans.append(nums[dq[0]])

        return ans
            



        
        