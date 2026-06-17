class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':        # edge case
            return 0

        prev2, prev1 = 1, 1             # dp[i-2], dp[i-1]

        for i in range(1, len(s)):
            current = 0

            # single digit decode — valid if current digit is not '0'
            if s[i] != '0':
                current += prev1

            # two digit decode — valid if between 10 and 26
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2

            prev2 = prev1
            prev1 = current
    
        return prev1
        