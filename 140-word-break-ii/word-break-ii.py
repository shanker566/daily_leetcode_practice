from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        n = len(s)

        @cache
        def dfs(start: int) -> list[str]:
            if start == n:
                return [""]

            sentences = []
            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word in word_set:
                    for sub_sentence in dfs(end):
                        if sub_sentence:
                            sentences.append(word + " " + sub_sentence)
                        else:
                            sentences.append(word)
            return sentences

        return dfs(0)
