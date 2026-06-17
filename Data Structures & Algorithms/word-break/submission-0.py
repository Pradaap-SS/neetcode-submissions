class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)          # O(1) lookup
        dp = [False] * (len(s) + 1)
        dp[0] = True                      # base case: empty string

        for i in range(1, len(s) + 1):         # end of substring
            for j in range(i):                 # start of substring
                if dp[j] and s[j:i] in word_set:   # valid split?
                    dp[i] = True
                    break                      # no need to check further

        return dp[len(s)]