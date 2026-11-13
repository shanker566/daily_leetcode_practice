class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        max_len = max((len(w) for w in wordDict), default=0)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Fixed: Set index 0 to True, not the whole list

        for i in range(1, n + 1):
            start = max(0, i - max_len)
            for j in range(start, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
