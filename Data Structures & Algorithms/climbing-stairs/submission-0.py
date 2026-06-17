class Solution:
    def climbStairs(self, n: int) -> int:
        # ways(n) = ways(n-1) + ways(n-2)
        if n <= 2:
            return n
        
        prev2, prev1 = 1, 2          # ways(1), ways(2)
        
        for i in range(3, n + 1):
            current = prev1 + prev2  # ways(n) = ways(n-1) + ways(n-2)
            prev2 = prev1
            prev1 = current
        
        return prev1



        